from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    #phonenumber = models.CharField(max_length=10)
    pass


class Category(models.Model):
    name = models.CharField(max_length=200)


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255, blank=False, null=False,
                            help_text="Enter a short description of the item")
    item_description = models.TextField(max_length=1200, blank=False, null=False,
                            help_text="Enter a brief description of the item")
    item_image = models.ImageField(upload_to='auctions/static/itemimage', height_field=None, width_field=None, max_length=100)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, null=True)
    expires = models.DateTimeField(editable=False, null=True)


class Auction(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    winner = models.ForeignKey(User, related_name='Auction_Winner',
                                blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, null=True)
    expires = models.DateTimeField(editable=False, null=True)
