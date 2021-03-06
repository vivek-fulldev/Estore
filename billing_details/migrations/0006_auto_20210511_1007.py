# Generated by Django 3.1.5 on 2021-05-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_details', '0005_auto_20210510_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payement_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=100)),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_signature', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Payment Detail',
            },
        ),
        migrations.AddField(
            model_name='billing_details',
            name='is_paid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
