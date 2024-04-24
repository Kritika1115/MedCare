from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User
from django.utils import timezone
from dashboard.models import *
from dashboard.forms import *


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
   apr_patient = User.objects.filter(date_joined__month=4).filter(is_patient=True).count()
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


   user_appointment = Appointments.objects.filter(patient=request.user).order_by('-id')
   specific_appointment  = Appointments.objects.filter(user=request.user).order_by('-id')
  
   context = {
       'specific_appointment' :  specific_appointment,
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
   if request.user.is_superuser:
       appointment = Appointments.objects.all()
   elif request.user.is_doctor:
       appointment = Appointments.objects.filter(user=request.user)
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
           appointment.patient = request.user
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




@login_required(login_url='/')
def generate_bill(request):
   if request.method == 'POST':
       form = GenerateBillForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, "Successfully generated bill")
           return redirect("dashboard:dashboard_page")
   else:
       form = GenerateBillForm()
   return render(request, 'dashboard/bills/add.html', {'form': form})


@login_required(login_url='/')
def update_bill(request, id):
   bill = Bills.objects.filter(id=id).first()
   if request.method == 'POST':
       form = GenerateBillForm(request.POST, instance=bill)
       if form.is_valid():
           form.save()
           messages.success(request, "Successfully updated bill")
           return redirect("dashboard:list_bill")
   else:
       form = GenerateBillForm(instance=bill)
   return render(request, "dashboard/bills/update.html", {'form': form})


@login_required(login_url='/')
def list_bill(request):
   bill = Bills.objects.all()
   context = {
       'bill': bill
       }
   return render(request,"dashboard/bills/list.html", context)


@login_required(login_url='/')
def generate_bill_items(request, bill_id):
   if request.method == 'POST':
       form = AddBillItemForm(request.POST)
       mainbill = Bills.objects.get(id=bill_id)
       if form.is_valid():
           bill = form.save(commit=False)
           bill.bills = mainbill
           bill.save()
           messages.success(request, "Successfully added items bill")
           return redirect("dashboard:bill_item_list", bill_id=bill_id)
   else:
       form = AddBillItemForm()
   return render(request, 'dashboard/bills/item/add.html', {'form': form})


@login_required(login_url='/')
def bill_item_list(request, bill_id):
   mainbill = Bills.objects.get(id=bill_id)
   billitem = BillsItems.objects.filter(bills=mainbill)
   context = {
       'billitem': billitem,
       'bill_id': bill_id,
       }
   return render(request,"dashboard/bills/item/list.html", context)


@login_required(login_url='/')
def delete_bill_item(request, bill_id, item_id):
   billitem = BillsItems.objects.filter(id=item_id).first()
   billitem.delete()
   messages.success(request, "Successfully deleted items bill")
   return redirect("dashboard:bill_item_list", bill_id=bill_id)




@login_required(login_url='/')
def customer_bills(request, app_id):
   cbill = Bills.objects.filter(appointment=app_id).first()
   context = {
       'cbill': cbill
       }
   return render(request,"dashboard/bills/customer_bill.html", context)


@login_required(login_url='/')
def customer_report(request, app_id):
   report = Appointments.objects.filter(id=app_id).first()
   context = {
       'report': report
       }
   return render(request,"dashboard/report/report.html", context)




@login_required(login_url='/')
def Paitent_history(request):
   if request.method == 'POST':
       form = PatientHistoryForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, "Successfully added Patient History")
           return redirect("dashboard:Paitent_history_list")
   else:
       form = PatientHistoryForm()
   return render(request, 'dashboard/patienthistory/add.html', {'form': form})


@login_required(login_url='/')
def Paitent_history_list(request):
   phistory = PatientHistory.objects.all()
   context = {
       'phistory': phistory
       }
   return render(request,"dashboard/patienthistory/list.html", context)


@login_required(login_url='/')
def Paitent_history_update(request, id):
   phistory = PatientHistory.objects.filter(id=id).first()
   if request.method == 'POST':
       form = PatientHistoryForm(request.POST, instance=phistory)
       if form.is_valid():
           form.save()
           messages.success(request, "Successfully updated paitent histroy")
           return redirect("dashboard:")
   else:
       form = PatientHistoryForm(instance=phistory)
   return render(request, "dashboard/patienthistory/update.html", {'form': form})


@login_required(login_url='/')
def search_by_pin(request):
   context = {}
   if request.method == 'GET':
       search_pin = request.GET.get('search_pin')
       if search_pin:
           phistory = PatientHistory.objects.filter(pin=search_pin).first()
           context['phistory'] = phistory
   return render(request, "dashboard/search/search.html", context)

