from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import User
from .models import Comment
from .models import Item
from .models import Category
from .forms import CommentForm, NewItemForm


def index(request):
    items = Item.objects.order_by('expires')
    context = {'items': items,}
    return render(request, "auctions/index.html", context)



def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print('item_name', form.cleaned_data.get('item_name'),
                    'item_description', form.cleaned_data.get('item_description'),
                    "item_category", form.cleaned_data.get('item_category'),
                    'ittem_bid', form.cleaned_data.get('item_bid'),
                    'item_image', form.cleaned_data.get('item_image'),
                    )
            obj = Item(item_image=request.FILES['item_image'])
            obj.user = request.user
            obj.item_name = form.cleaned_data.get('item_name')
            obj.item_description = form.cleaned_data.get('item_description')
            obj.item_category = form.cleaned_data.get('item_category')
            obj.item_bid = form.cleaned_data.get('item_bid')
            obj.item_image = form.cleaned_data.get('item_image')
            
            '''instance = Item(item_image=request.FILES['item_image'])
            instance.save()'''
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



def item_page(request):
    pass


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