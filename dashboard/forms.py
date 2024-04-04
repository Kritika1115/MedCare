from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from dashboard.models import *

class DoctorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'phone', 'dob', 'specialization', 'address','password1','password2')

class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'phone', 'dob', 'address')
        
class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('patient_name','user', 'patient_problem', 'appointment_date', 'phone', 'doctor_dignosis', 'doctor_pescription', 'is_accepted', 'is_checked_by_doctor')

        labels = {
            "user" : "Choose doctor *"
        }

class AppointmentbookForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('patient_name','user', 'patient_problem', 'appointment_date', 'phone')

        labels = {
            "user" : "Choose doctor *"
        }
        
class GenerateBillForm(forms.ModelForm):
    class Meta:
        model = Bills
        fields = ('patient', 'appointment', 'bill_no', 'sub_total', 'discount', 'net_amount', 'paid_status')

        labels = {
            "patient" : "patient"
        }

class AddBillItemForm(forms.ModelForm):
    class Meta:
        model = BillsItems
        fields = ('description', 'qty', 'amount')
