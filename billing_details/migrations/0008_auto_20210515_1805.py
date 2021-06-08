# Generated by Django 3.1.5 on 2021-05-15 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_registration'),
        ('billing_details', '0007_billing_details_anonmyous_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='anonmyous_user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_profiles.anonmyous_user'),
        ),
    ]