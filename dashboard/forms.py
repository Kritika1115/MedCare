from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class DoctorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'phone', 'dob', 'address','password1','password2']
