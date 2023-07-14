from django import forms
from django.contrib.auth.models import User
from .models import Item, Category


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'description', 'price', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
