# Generated by Django 4.2 on 2024-03-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]