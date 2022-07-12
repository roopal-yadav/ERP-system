# Generated by Django 4.0.5 on 2022-07-08 06:20

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0005_subjects'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='subjects',
            managers=[
                ('sub_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='branch_detail',
            name='subject',
            field=models.ManyToManyField(to='branch.subjects'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
