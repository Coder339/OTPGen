# Generated by Django 3.0.5 on 2020-08-14 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretkey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otpmodel',
            name='phone',
        ),
    ]