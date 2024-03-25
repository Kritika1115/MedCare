from django.urls import path
from dashboard import views as dashboard

app_name = "dashboard"
urlpatterns = [
    path("dashboard/", dashboard.dashboard_page, name="dashboard_page"),
    path("adddoctor/", dashboard.add_doctor, name="add_doctor"),
    path("doctors/", dashboard.list_doctor, name="list_doctor"),
    path("doctors/delete/<int:id>", dashboard.delete_doctor, name="delete_doctor"),
]