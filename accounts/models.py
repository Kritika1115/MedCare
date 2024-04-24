from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others'),
    )
    email = models.EmailField(unique=True, verbose_name='email')
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    specialization = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    profile_pic = models.ImageField(upload_to='profile', default='profile/user.jpg')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username","first_name","last_name" 

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.specialization + "-" + self.email