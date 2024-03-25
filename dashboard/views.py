from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Appointments
from dashboard.forms import DoctorRegisterForm
from django.contrib import messages
from accounts.models import User

# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    appointments = Appointments.objects.all()
    context = {
        'appointment': appointments
    }
    return render(request,'dashboard/dashboard.html', context)


@login_required(login_url='/')
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_doctor = True
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Successfully added doctor")
    else:
        form = DoctorRegisterForm()
    return render(request, 'dashboard/doctor/add.html', {'form': form})

@login_required(login_url='/')
def list_doctor(request):
    doctor = User.objects.filter(is_doctor=True)
    context = {
        'doctors': doctor
        }
    return render(request,"dashboard/doctor/list.html", context)