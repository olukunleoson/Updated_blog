from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class Registration_form(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=30, required=True)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=20, required=True)

    class Meta(forms.ModelForm):
        model = Comment
        fields = ('name', 'email',)