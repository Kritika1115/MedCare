from django.db import models
from accounts.models import User


# Create your models here.
class Appointments(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user', limit_choices_to={'is_doctor': True} )
   patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='patient', limit_choices_to={'is_patient': True} )
   patient_problem = models.TextField()
   appointment_date = models.DateField()
   created_date = models.DateTimeField(auto_now_add=True)
   phone = models.IntegerField()
   doctor_dignosis = models.TextField()
   doctor_pescription = models.TextField()
   is_accepted = models.BooleanField(default=False)
   is_checked_by_doctor = models.BooleanField(default=False)
   updated_date = models.DateTimeField(auto_now=True)


   class Meta:
       verbose_name = 'appointment'


   def __str__(self):
       return "name:" + self.user.first_name + self.user.last_name +  "appointment:"+ self.patient_name + self.user.email


class Bills(models.Model):
   patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billspatient', limit_choices_to={'is_patient': True} )
   appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, related_name='billspatient')
   bill_no = models.IntegerField(unique=True)
   created_date = models.DateTimeField(auto_now_add=True)
   sub_total = models.CharField(max_length=10)
   discount = models.CharField(max_length=10)
   net_amount = models.CharField(max_length=10)
   paid_status = models.BooleanField(default=False)


   class Meta:
       verbose_name = 'bill'


   def __str__(self):
       return self.patient.first_name + self.patient.last_name + ":billno" + str(self.bill_no)
  
class BillsItems(models.Model):
   bills = models.ForeignKey(Bills, on_delete=models.CASCADE, related_name='billitem')
   description = models.CharField(max_length=255)
   qty = models.CharField(max_length=255, null=True, blank=True)
   amount = models.IntegerField()


   class Meta:
       verbose_name = 'billitem'


   def __str__(self):
       return self.bills.patient.first_name


class PatientHistory(models.Model):
   patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patienthistory', limit_choices_to={'is_patient': True} )
   pin = models.IntegerField()
   blood_type = models.CharField(max_length=255, null=True, blank=True)
   allergies = models.TextField(null=True, blank=True)
   illness = models.TextField(null=True, blank=True)
   surgery = models.TextField(null=True, blank=True)
   medicine_taken = models.TextField(null=True, blank=True)
   immunization = models.TextField(null=True, blank=True)
   vitals = models.TextField(null=True, blank=True)
   weight = models.CharField(max_length=255, null=True, blank=True)
   heart_rate = models.CharField(max_length=255, null=True, blank=True)
   blood_pressure = models.TextField(null=True, blank=True)


   class Meta:
       verbose_name = 'patienthistory'
       verbose_name_plural = 'patienthistory'


   def __str__(self):
       return self.patient.first_name + self.patient.last_name

