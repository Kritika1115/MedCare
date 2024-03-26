from django.urls import path
from dashboard import views as dashboard

app_name = "dashboard"
urlpatterns = [
    path("dashboard/", dashboard.dashboard_page, name="dashboard_page"),
    path("adddoctor/", dashboard.add_doctor, name="add_doctor"),
    path("doctors/", dashboard.list_doctor, name="list_doctor"),
    path("doctors/delete/<int:id>", dashboard.delete_doctor, name="delete_doctor"),
    path("doctors/update/<int:id>", dashboard.update_doctor, name="update_doctor"),
    path("appointment/", dashboard.appointment_list_admin, name="appointment_list_admin"),
    path("appointment/delete/<int:id>", dashboard.delete_appointment, name="delete_appointment"),
    path("appointment/update/<int:id>", dashboard. update_appointment, name="update_appointment"),
]