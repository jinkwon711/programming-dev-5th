from django.forms import ModelForm
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput
from .models import ZipCode, Comment, Post
from django import forms
import re


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','tags', 'lnglat']

class ZipCodeForm(forms.ModelForm):
    class Meta:
        model = ZipCode
        fields = ['zipcode',]


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'author']