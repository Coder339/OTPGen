# Generated by Django 3.0.5 on 2020-08-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretkey', '0005_otpmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
