# Generated by Django 4.2 on 2024-04-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_bills_remove_report_patient_name_report_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bill_no',
            field=models.IntegerField(unique=True),
        ),
    ]