# Generated by Django 5.1.3 on 2024-11-25 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_donation_donationname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='donatiodate',
            new_name='donationdate',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='volunteermark',
            new_name='volunteerremark',
        ),
    ]
