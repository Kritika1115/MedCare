# Generated by Django 4.2 on 2024-04-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_address_user_dob_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='specialization',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
