# Generated by Django 4.2 on 2024-04-01 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_appointments_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='doctor_name',
        ),
    ]
