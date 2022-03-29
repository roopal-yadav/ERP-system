# Generated by Django 3.2 on 2022-03-29 04:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacherlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherid', models.CharField(max_length=20)),
                ('teacherpwd', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(8, 'the field must contain at least 50 characters')])),
            ],
        ),
    ]
