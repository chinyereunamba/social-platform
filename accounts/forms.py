from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']