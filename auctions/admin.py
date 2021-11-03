from django.contrib import admin

# Register your models here.
from .models import Comment
from .models import Category
from .models import Item

admin.site.register(Item)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'item', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(active=True)