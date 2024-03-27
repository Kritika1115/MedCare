from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Appointments
from dashboard.forms import DoctorRegisterForm, DoctorUpdateForm, AppointmentUpdateForm
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
            return redirect("dashboard:list_doctor")
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

@login_required(login_url='/')
def delete_doctor(request, id):
    doctor = User.objects.filter(is_doctor=True, id=id).first()
    doctor.delete()
    return redirect("dashboard:list_doctor")

@login_required(login_url='/')
def update_doctor(request, id):
    doctor = User.objects.filter(is_doctor=True, id=id).first()
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=doctor)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_doctor = True
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Successfully updated doctor")
            return redirect("dashboard:list_doctor")
    else:
        form = DoctorUpdateForm(instance=doctor)
    return render(request, "dashboard/doctor/update.html", {'form': form})

@login_required(login_url='/')
def appointment_list_admin(request):
    appointment = Appointments.objects.all()
    return render(request, "dashboard/appointment/list.html", {"appointment": appointment})

@login_required(login_url='/')
def delete_appointment(request, id):
    appointment = Appointments.objects.filter(id=id).first()
    appointment.delete()
    return redirect("dashboard:appointment_list_admin")

@login_required(login_url='/')
def update_appointment(request, id):
    appointment = Appointments.objects.filter(id=id).first()
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, "Successfully updated appointment")
            return redirect("dashboard:appointment_list_admin")
    else:
        form = AppointmentUpdateForm(instance=appointment)
    return render(request, "dashboard/doctor/update.html", {'form': form})

@login_required(login_url='/')
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, "Successfully added appointment")
            return redirect("dashboard:appointment_list_admin")
    else:
        form = AppointmentUpdateForm()
    return render(request, 'dashboard/appointment/add.html', {'form': form})

@login_required(login_url='/')
def patient_list(request):
    patient = User.objects.filter(is_patient=True)
    return render(request, "dashboard/patient/list.html", {"patients":patient})

@login_required(login_url='/')
def delete_patient(request, id):
    patient = User.objects.filter(id=id).first()
    patient.delete()
    return redirect("dashboard:patient_list")