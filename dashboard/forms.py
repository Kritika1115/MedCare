from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from dashboard.models import Appointments

class DoctorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'phone', 'dob', 'address','password1','password2')

class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'phone', 'dob', 'address')
        
class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('patient_name','doctor_name', 'doctor_specialization', 'patient_problem', 'phone', 'notes')