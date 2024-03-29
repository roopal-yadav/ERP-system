# Generated by Django 4.0.5 on 2022-07-08 05:57

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_remove_lec_fac_remove_lec_loc_remove_lec_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='lec',
        ),
        migrations.AlterModelManagers(
            name='branch_detail',
            managers=[
                ('branch_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='branch_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='branch_detail',
            name='name',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='timetable',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch_detail'),
        ),
    ]
