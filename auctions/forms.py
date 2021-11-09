from .models import Comment
from django import forms
from .models import Category, Item


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'item', 'body')


class MakeBidForm(forms.Form):
    bid = forms.DecimalField(required=True, 
                        widget=forms.NumberInput(
                            attrs={"id": "new_bid",
                                "name": "new_bid",
                                "class": "form-control w-100",
                                "inputmode": "decimal",
                                'placeholder': 0.00,
                                'min': 0,
                                'step': 1,
                                'title': "Place Your bid here"
                            }, ))
class NewItemForm(forms.Form):
    item_name = forms.CharField(required=True,
                        widget=forms.TextInput(
                            attrs={'value': '',
                                "class": "form-control",
                                "id": "item_name",
                                "name": "item_name",
                                "aria-describedby": "item_name",
                                'placeholder': 'Some like Iphone 12',
                                #'maxlength': Item.item_name.max_length,
                                'maxlength': Item._meta.get_field('item_name').max_length,
                                }))
    item_description = forms.CharField(required=True, 
                        widget=forms.Textarea(
                            attrs={'value': '',
                                    "id": "item_description",
                                    "name": "item_description",
                                    "rows": 10,
                                    "class": "form-control",
                                    'placeholder': 'Place description here',
                                    #'maxlength': Item.item_description.max_length,
                                    'maxlength': Item._meta.get_field('item_description').max_length,
                                    }))
    item_category = forms.ModelChoiceField(required=True,
                        queryset=Category.objects.order_by('category_id'), 
                        widget=forms.Select(
                            attrs={"class": "form-control w-auto",
                                "id": "item_category",
                                "name": "item_category",
                            }), )
    item_start_price = forms.DecimalField(required=True, 
                        widget=forms.NumberInput(
                            attrs={"id": "item_description",
                                "name": "item_description",
                                "class": "form-control w-25",
                                "inputmode": "decimal",
                                'placeholder': 0.00,
                                'min': 0,
                                'step': 1,
                                'title': "Place Your bid here"
                            }, ))
    item_image = forms.FileField(required=True,
                        widget=forms.ClearableFileInput(
                            attrs={"id": "item_image",
                                "name": "item_image",
                                "class": "custom-file-input",
                                "accept": "image/*",
                            }, ))


class AddBidForm(forms.Form):
    item_bid = forms.DecimalField(required=True, 
                        widget=forms.NumberInput(
                            attrs={"id": "item_description",
                                "name": "item_description",
                                "class": "form-control w-25",
                                "inputmode": "decimal",
                                'placeholder': 0.00,
                                'min': 0,
                                'step': 1,
                                'title': "Place Your bid here"
                            }, ))


class CommentForm(forms.Form):
    item_description = forms.CharField(required=True, 
                        widget=forms.Textarea(
                            attrs={'value': '',
                                    "id": "item_description",
                                    "name": "item_description",
                                    "rows": 10,
                                    "class": "form-control",
                                    'placeholder': 'Place description here',
                                    #'maxlength': Item.item_description.field.max_length,
                                    'maxlength': Item._meta.get_field('item_description').max_length,
                                    }))


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
                                    
    def __init__(self, *args, **kwargs):
        super(NewItemForm, self).__init__(*args, **kwargs)
        if kwargs.get('initial'):
            if kwargs.get('initial').get('item_name_readonly'):
                self.fields['item_name'].widget.attrs['readonly'] = True """