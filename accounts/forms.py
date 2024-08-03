from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ["email", "display_name", "username", "password1", "password2"]

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bio', 'profile_pic', 'display_name']