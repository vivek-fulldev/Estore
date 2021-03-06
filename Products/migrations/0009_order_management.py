# Generated by Django 3.1.5 on 2021-05-06 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_coupon_management_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('total_amt', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products')),
            ],
            options={
                'verbose_name': 'Order Product',
            },
        ),
    ]
