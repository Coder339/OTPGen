# Generated by Django 3.0.5 on 2020-08-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200816_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='otp',
            new_name='phone',
        ),
    ]
