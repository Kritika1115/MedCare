from django.contrib import admin
from dashboard.models import (
    Appointments, 
    Report,
    Bills,
    BillsItems,
    PatientHistory,
)
# Register your models here.

admin.site.register(Appointments)
admin.site.register(Report)
admin.site.register(Bills)
admin.site.register(BillsItems)
admin.site.register(PatientHistory)