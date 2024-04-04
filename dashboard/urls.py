from django.urls import path
from dashboard import views as dashboard

app_name = "dashboard"
urlpatterns = [
    path("dashboard/", dashboard.dashboard_page, name="dashboard_page"),

    path("adddoctor/", dashboard.add_doctor, name="add_doctor"),
    path("doctors/", dashboard.list_doctor, name="list_doctor"),
    path("doctors/delete/<int:id>/", dashboard.delete_doctor, name="delete_doctor"),
    path("doctors/update/<int:id>/", dashboard.update_doctor, name="update_doctor"),

    path("appointment/", dashboard.appointment_list_admin, name="appointment_list_admin"),
    # path("appointment/patient/", dashboard.appointment_list_patient, name="appointment_list_patient"),
    path("appointment/delete/<int:id>/", dashboard.delete_appointment, name="delete_appointment"),
    path("appointment/update/<int:id>/", dashboard.update_appointment, name="update_appointment"),
    path("appointment/add/", dashboard.add_appointment, name="add_appointment"),

    path("patient/", dashboard.patient_list, name="patient_list"),
    path("patient/delete/<int:id>/", dashboard.delete_patient, name="delete_patient"),

    path("bills/", dashboard.list_bill, name="list_bill"),
    path("bills/add/", dashboard.generate_bill, name="generate_bill"),
    path("bills/update/<int:id>/", dashboard.update_bill, name="update_bill"),

    path("billitem/<int:bill_id>/", dashboard.bill_item_list, name="bill_item_list"),
    path("billitem/<int:bill_id>/add/", dashboard.generate_bill_items, name="generate_bill_items"),
    path("billitem/<int:bill_id>/delete/<int:item_id>/", dashboard.delete_bill_item, name="delete_bill_item"),
]