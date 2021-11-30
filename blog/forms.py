from django import forms
from django.forms import fields
from .models import *


class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Your email'}),
            'body': forms.Textarea(attrs={'class': 'form-control no-resize', 'rows': "4", 'placeholder': 'Please type what you want...'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'image', 'category', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control no-resize', 'rows': "4", 'placeholder': 'Please type what you want...'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category name'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag name'}),
        }
