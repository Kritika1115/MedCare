# Generated by Django 4.2 on 2024-04-04 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0012_appointments_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField()),
                ('patient_address', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.CharField(max_length=10)),
                ('discount', models.CharField(max_length=10)),
                ('net_amount', models.CharField(max_length=10)),
                ('patient', models.ForeignKey(blank=True, limit_choices_to={'is_patient': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billspatient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='report',
            name='patient',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_patient': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportpatient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BillsItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('bills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billitem', to='dashboard.bills')),
            ],
        ),
    ]
