from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages

import uuid

from .models import User
from .models import Comment
from .models import Item
from .models import Category
from .models import Bid
from .models import Favorite
from .forms import CommentForm, NewItemForm, MakeBidForm


def index(request, category=None, favorite=None):
    page_head = None
    items = Item.objects.order_by('expires') 
    categoryes = Category.objects.all()
    if category:
        category = get_object_or_404(Category, category=category)
        items = Item.objects.filter(item_category=category)
        page_head = category
    if favorite:
        if request.user:
            items = Favorite.objects.filter(user=request.user).order_by('expires') 
            page_head = "Favorites"
    context = {'items': items,
                'page_head': page_head or None,
                'categoryes': categoryes}
    return render(request, "auctions/index.html", context)


def favorites(request, favorite=True):
    if favorite:
        return index(request, favorite)
    else:
        return index(request)

def new_item(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewItemForm(request.POST, request.FILES)
            print('request.FILES', request.FILES)
            if form.is_valid():             

                obj = Item(item_image=request.FILES['item_image'])
                obj.user = request.user
                obj.item_name = form.cleaned_data.get('item_name')
                obj.item_description = form.cleaned_data.get('item_description')
                obj.item_category = form.cleaned_data.get('item_category') 
                obj.item_start_price = form.cleaned_data.get('item_start_price')
                #obj.item_bid = form.cleaned_data.get('item_bid')
                obj.item_image = form.cleaned_data.get('item_image')                
                obj.save()
                messages.success(request, 'New Auction Created')
            else:
                print("Form invalid")
                messages.error(request, 'Error creating Auction. Not valid form')
                return render(request, "auctions/new_item.html",
                        context = {'form': form,})
            return render(request, "auctions/new_item.html",
                        context = {'form': form,
                        "message": "Form Submitted"})
        else:
            categoryes = Category.objects.order_by('category_id')
            form = NewItemForm()
            context = {'categoryes': categoryes,
                        'form': form}
            messages.info(request, 'Test message')
            return render(request, "auctions/new_item.html",
                        context)
    else:
        return render(request, "auctions/login.html")


def item_page(request, item_UUID=None):
    if item_UUID:
        item = Item.objects.get(item_UUID=item_UUID)
        item_bids = Bid.objects.filter(item=item).order_by('created').reverse()
        current_price = float(item_bids[0].bid) if len(item_bids)>0 else float(item.item_start_price)
        bids_total = len(item_bids) if len(item_bids)>0 else 0
        print('current_price', current_price)
        print('item_bids', item_bids)
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            form = MakeBidForm(request.POST)
            if form.is_valid():
                new_bid = form.cleaned_data.get('bid')
                if new_bid > current_price:                    
                    obj = Bid()
                    obj.user = user
                    obj.item = item
                    obj.bid = new_bid
                    obj.save()
                    item.item_current_price = new_bid
                    item.item_bids_count = bids_total + 1
                    item.save()
                    messages.success(request, 'Your bid accepted')
                else:
                    messages.error(request, 'Your bid not accepted')
        item_bids = Bid.objects.filter(item=item).order_by('created').reverse()
        current_price = float(item_bids[0].bid) if len(item_bids)>0 else float(item.item_start_price)
        bids_total = len(item_bids) if len(item_bids)>0 else 0
        recomended_price = current_price + .01
        favorite = True if Favorite.objects.filter(item=item) else False
        context = {'item': item,
                'current_price': current_price,
                'recomended_price': recomended_price,
                'favorite': favorite,
                'bids_total':bids_total,
                'bid_form': MakeBidForm}
        return render(request, "auctions/item.html",
                context)
    else:
        messages.error(request, 'You are not signed')
        return render(request, "auctions/login.html")


def add_to_favorites(request, item_UUID=None):
    #item_UUID = request.POST.get('userbooks')
    if request.method == 'POST':
        print("add_to_watchlist")
        item = Item.objects.get(item_UUID=item_UUID)
        if Favorite.objects.filter(user=request.user, item=item):
            fav = Favorite.objects.get(user=request.user, item=item)
            fav.delete()
            return JsonResponse({'success':True})
        else:
            fav = Favorite(user=request.user, item=item)
            fav.save()
            return JsonResponse({'success':True})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Succefull.')
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                #"message": "Invalid username and/or password.",
                "message": messages.error(request, 'Invalid username and/or password.'),
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out.')
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Comment, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})