from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe

from datetime import datetime, timedelta
from random import randrange
import uuid
import os
from sorl.thumbnail import ImageField


ITEM_CODE_MAX_TRIES = 32
CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'

def path_and_rename(instance, filename):
    upload_to = 'auctions/static/itemimage'
    filename = f'{instance.item_UUID}_{filename}'    
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
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category



class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_UUID = models.UUIDField(default=uuid.uuid4, max_length=36, editable=False, null= True, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    item_name = models.CharField(max_length=255, blank=False, null=False,
                            help_text="Enter a short description of the item")
    item_description = models.TextField(max_length=1200, blank=False, null=False,
                            help_text="Enter a brief description of the item")
    item_image = models.ImageField(upload_to=path_and_rename,
                        null= True, blank=True,
                        height_field=None, width_field=None, max_length=200)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_start_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0, blank=True, null=True,)
    item_current_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    item_bids_count = models.IntegerField(default=0)
    #item_bid = models.ForeignKey(Bid, on_delete=models.CASCADE)

    created = models.DateTimeField(editable=False, null=True,
                                auto_now_add=True)
    expires = models.DateTimeField(editable=True, null=True,
                                default=datetime.now()+timedelta(days=30))


    def __str__(self):
        return f'{self.item_id}: {self.item_UUID}: {self.item_name}' 

    '''def save(self, *args, **kwargs):
        """
        https://github.com/workmajj/django-unique-random/blob/master/unique_random/models.py
        """
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < ITEM_CODE_MAX_TRIES:
                new_code = str(uuid.uuid4())
                if not Item.objects.filter(item_code=new_code):
                    self.item_code = new_code
                    unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Item, self).save(*args, **kwargs)'''


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    bid = models.DecimalField(max_digits=20, decimal_places=2,
                                default=0.0, null= True, blank=True,)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, null=True,
                                auto_now_add=True)
    def __str__(self):
        return f'{self.user}: bid {self.bid} at {self.created}'



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



