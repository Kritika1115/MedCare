from django.contrib import admin
from dashboard.models import (
    Appointments, 
    Report,
)
# Register your models here.

admin.site.register(Appointments)
admin.site.register(Report)