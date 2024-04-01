from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Appointments
from dashboard.forms import DoctorRegisterForm, DoctorUpdateForm, AppointmentUpdateForm, AppointmentbookForm
from django.contrib import messages
from accounts.models import User
from django.utils import timezone

# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    appointments = Appointments.objects.filter(created_date__date=timezone.now().date())
    jan_appointment = Appointments.objects.filter(created_date__month=1).count()
    feb_appointment = Appointments.objects.filter(created_date__month=2).count()
    mar_appointment = Appointments.objects.filter(created_date__month=3).count()
    apr_appointment = Appointments.objects.filter(created_date__month=4).count()
    may_appointment = Appointments.objects.filter(created_date__month=5).count()
    june_appointment = Appointments.objects.filter(created_date__month=6).count()
    july_appointment = Appointments.objects.filter(created_date__month=7).count()
    aug_appointment = Appointments.objects.filter(created_date__month=8).count()
    sep_appointment = Appointments.objects.filter(created_date__month=9).count()
    oct_appointment = Appointments.objects.filter(created_date__month=10).count()
    nov_appointment = Appointments.objects.filter(created_date__month=11).count()
    dec_appointment = Appointments.objects.filter(created_date__month=12).count()
    
    jan_patient = User.objects.filter(date_joined__month=1).count()
    feb_patient = User.objects.filter(date_joined__month=2).count()
    mar_patient = User.objects.filter(date_joined__month=3).count()
    apr_patient = User.objects.filter(date_joined__month=4).count()
    may_patient = User.objects.filter(date_joined__month=5).count()
    june_patient = User.objects.filter(date_joined__month=6).count()
    july_patient = User.objects.filter(date_joined__month=7).count()
    aug_patient = User.objects.filter(date_joined__month=8).count()
    sep_patient = User.objects.filter(date_joined__month=9).count()
    oct_patient = User.objects.filter(date_joined__month=10).count()
    nov_patient = User.objects.filter(date_joined__month=11).count()
    dec_patient = User.objects.filter(date_joined__month=12).count()
    
    
    total_patient = User.objects.filter (is_patient=True).count()
    total_doctor = User.objects.filter (is_doctor=True).count()
    total_appointment = Appointments.objects.filter(created_date__date=timezone.now().date()).count()

    user_appointment = Appointments.objects.filter(user=request.user).order_by('-id')
    
    context = {
        'user_appointment' :  user_appointment,
        'total_patient' :  total_patient,
        'total_doctor' :  total_doctor,
        'total_appointment' : total_appointment,
        'appointment': appointments,
        'jan' : jan_appointment,
        'feb' : feb_appointment,
        'mar' : mar_appointment,
        'apr' : apr_appointment,
        'may' : may_appointment,
        'june': june_appointment,
        'july' : july_appointment,
        'aug' : aug_appointment,
        'sep' : sep_appointment,
        'oct' : oct_appointment,
        'nov' : nov_appointment,
        'dec' : dec_appointment,
        
        'pjan' : jan_patient,
        'pfeb' : feb_patient,
        'pmar' : mar_patient,
        'papr' : apr_patient,
        'pmay' : may_patient,
        'pjune': june_patient,
        'pjuly' : july_patient,
        'paug' : aug_patient,
        'psep' : sep_patient,
        'poct' : oct_patient,
        'pnov' : nov_patient,
        'pdec' : dec_patient
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

# @login_required(login_url='/')
# def appointment_list_patient(request):
#     appointment = Appointments.objects.filter(user=request.user)
#     return render(request, "dashboard/appointment/patientlist.html", {"appointment": appointment})

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
    return render(request, "dashboard/appointment/update.html", {'form': form})

@login_required(login_url='/')
def add_appointment(request):
    if request.method == 'POST':
        if request.user.is_patient:
            form = AppointmentbookForm(request.POST)
        else:
            form = AppointmentUpdateForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            if request.user.is_patient:
                messages.success(request, "Successfully booked appointment")
                return redirect("dashboard:dashboard_page")
            else:
                messages.success(request, "Successfully added appointment")
                return redirect("dashboard:appointment_list_admin")
    else:
        if request.user.is_patient:
            form = AppointmentbookForm()
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