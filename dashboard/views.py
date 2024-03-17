from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Appointments

# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    appointments = Appointments.objects.all()
    context = {
        'appointment': appointments
    }
    return render(request,'dashboard/dashboard.html', context)
