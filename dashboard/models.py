from django.db import models
from accounts.models import User

# Create your models here.
class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user' )
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    doctor_specialization = models.CharField(max_length=255)
    patient_problem = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        verbose_name = 'appointment'

    def __str__(self):
        return self.patient_name
    
class Report(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )
    patient_name = models.CharField(max_length=255)
    patient_address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    patient_dob = models.DateField()
    patient_phone = models.CharField(max_length=255)
    patient_gender = models.CharField(max_length=255, choices=GENDER)
    patient_diagonisis = models.TextField()

    class meta:
        verbose_name = 'report'

    def __str__(self):
        return self.patient_name
