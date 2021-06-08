# Generated by Django 3.1.5 on 2021-05-10 18:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('billing_details', '0004_auto_20210509_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='city',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Delhi', 'Delhi')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='email_address',
            field=models.EmailField(default='No Data', max_length=254),
        ),
        migrations.AlterField(
            model_name='billing_details',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]