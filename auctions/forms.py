from .models import Comment
from django import forms
from .models import Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'item', 'body')

class NewItemForm(forms.Form):
    item_name = forms.CharField(required=True, widget=forms.TextInput())
    item_description = forms.CharField(required=True, widget=forms.Textarea())
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    CHOICES = tuple(c.name for c in Category.objects.order_by('category_id'))
    print('CHOICES', CHOICES)
    item_category = forms.ChoiceField(choices=CHOICES)
    print('item_category', item_category)
    item_bid = forms.DecimalField(required=True, )



""" class NewItemForm(forms.Form):
    item_name = forms.CharField(required=True, 
                        widget=forms.TextInput(
                            attrs={'value': '',
                                "class": "form-control",
                                "id": "item_name",
                                "name": "item_name",
                                "aria-describedby": "item_name",
                                'required': 'true',
                                'placeholder': 'Some like Iphone 12'}))
    item_text = forms.CharField(
                        widget=forms.Textarea(
                            attrs={'value': '',
                                    "id": "item_description",
                                    "name": "item_description",
                                    "rows": 10,
                                    "class": "form-control",
                                    'required': 'true',
                                    'placeholder': 'Place description here'})) 
                                    
    def __init__(self, *args, **kwargs):
        super(NewItemForm, self).__init__(*args, **kwargs)
        if kwargs.get('initial'):
            if kwargs.get('initial').get('item_name_readonly'):
                self.fields['item_name'].widget.attrs['readonly'] = True """