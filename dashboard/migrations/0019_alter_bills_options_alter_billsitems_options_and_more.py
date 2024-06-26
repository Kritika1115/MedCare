# Generated by Django 4.2 on 2024-04-04 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0018_patienthistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bills',
            options={'verbose_name': 'bill'},
        ),
        migrations.AlterModelOptions(
            name='billsitems',
            options={'verbose_name': 'billitem'},
        ),
        migrations.AlterModelOptions(
            name='patienthistory',
            options={'verbose_name': 'patienthistory', 'verbose_name_plural': 'patienthistory'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'report'},
        ),
        migrations.AddField(
            model_name='bills',
            name='appointment',
            field=models.ForeignKey(default=29, limit_choices_to={'is_patient': True}, on_delete=django.db.models.deletion.CASCADE, related_name='billspatient', to='dashboard.appointments'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bills',
            name='patient',
            field=models.ForeignKey(default=29, limit_choices_to={'is_patient': True}, on_delete=django.db.models.deletion.CASCADE, related_name='billspatient', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
