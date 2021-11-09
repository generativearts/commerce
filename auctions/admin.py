from django.contrib import admin

# Register your models here.
from .models import Comment
from .models import Category
from .models import Item
from .models import Bid
from .models import Favorite

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Favorite)


""" @admin.register(Item)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields] """

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'item', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(active=True)