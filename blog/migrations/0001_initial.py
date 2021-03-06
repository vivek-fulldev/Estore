# Generated by Django 3.1.5 on 2021-05-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='', verbose_name=models.ImageField(upload_to='uploads/blog'))),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
