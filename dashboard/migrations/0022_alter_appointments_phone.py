# Generated by Django 4.2 on 2024-04-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_appointments_updated_date_patienthistory_pin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
