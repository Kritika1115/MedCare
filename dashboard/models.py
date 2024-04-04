from django.db import models
from accounts.models import User

# Create your models here.
class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user', limit_choices_to={'is_doctor': True} )
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='patient', limit_choices_to={'is_patient': True} )
    patient_name = models.CharField(max_length=255)
    patient_problem = models.TextField()
    appointment_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)
    doctor_dignosis = models.TextField()
    doctor_pescription = models.TextField()
    is_accepted = models.BooleanField(default=False)
    is_checked_by_doctor = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'appointment'

    def __str__(self):
        return self.user.first_name + " appointment"
    
class Report(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reportpatient', limit_choices_to={'is_patient': True} )
    doctor_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    patient_diagonisis = models.TextField()

    class Meta:
        verbose_name = 'report'

    def __str__(self):
        return self.patient.first_name

class Bills(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billspatient', limit_choices_to={'is_patient': True} )
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, related_name='billspatient')
    bill_no = models.IntegerField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    sub_total = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    net_amount = models.CharField(max_length=10)

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
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patienthistory', limit_choices_to={'is_patient': True} )
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