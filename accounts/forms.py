from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        Model = User
        fields = ["first_name", "last_name", "email", "password1"," password2"]