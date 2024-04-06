from dashboard.models import PatientHistory
from django.contrib.auth.models import AnonymousUser


def pin(request):
   if isinstance(request.user, AnonymousUser):
       return {"pin": None}
   else:
       try:
           phistory = PatientHistory.objects.get(patient=request.user)
           return {"pin": phistory.pin}
       except PatientHistory.DoesNotExist:
           return {"pin": None}




