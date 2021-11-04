from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe

from datetime import datetime, timedelta
import os
from sorl.thumbnail import ImageField


def path_and_rename(instance, filename):
    upload_to = 'auctions/static/itemimage'
    filename = f'{instance.item_id}_{filename}'    
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    username = models.CharField(primary_key=True, 
                            max_length=255, blank=False,
                            null=False, unique=True,
                            help_text="User name")
    phonenumber = models.CharField(max_length=10, unique=True, default="380")
    pass


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    item_name = models.CharField(max_length=255, blank=False, null=False,
                            help_text="Enter a short description of the item")
    item_description = models.TextField(max_length=1200, blank=False, null=False,
                            help_text="Enter a brief description of the item")
    item_image = models.ImageField(upload_to=path_and_rename, height_field=None, width_field=None, max_length=100)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=20, decimal_places=2,
                                default=0.1)
    created = models.DateTimeField(editable=False, null=True,
                                auto_now_add=True)
    expires = models.DateTimeField(editable=True, null=True,
                                default=datetime.now()+timedelta(days=30))


    def __str__(self):
        return f'{self.item_id}: {self.item_name}' 


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    bid = models.DecimalField(max_digits=20, decimal_places=2,
                                default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, null=True,
                                auto_now_add=True)



class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    body = models.TextField(max_length=600, blank=False, null=False,
                            help_text="Enter your comment")
    created_on = models.DateTimeField(editable=False, null=True,
                                auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.user} at {self.created_on}'



