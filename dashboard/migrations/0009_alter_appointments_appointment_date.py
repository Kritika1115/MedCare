# Generated by Django 4.2 on 2024-04-01 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_appointments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]