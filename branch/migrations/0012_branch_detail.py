# Generated by Django 4.0.5 on 2022-07-12 11:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0011_delete_branch_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch_detail',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('batch', models.IntegerField()),
                ('fri_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l1', to='branch.subjects')),
                ('fri_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l2', to='branch.subjects')),
                ('fri_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l3', to='branch.subjects')),
                ('fri_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l4', to='branch.subjects')),
                ('fri_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l5', to='branch.subjects')),
                ('fri_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l6', to='branch.subjects')),
                ('fri_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l7', to='branch.subjects')),
                ('fri_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri_l8', to='branch.subjects')),
                ('mon_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l1', to='branch.subjects')),
                ('mon_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l2', to='branch.subjects')),
                ('mon_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l3', to='branch.subjects')),
                ('mon_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l4', to='branch.subjects')),
                ('mon_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l5', to='branch.subjects')),
                ('mon_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l6', to='branch.subjects')),
                ('mon_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l7', to='branch.subjects')),
                ('mon_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_l8', to='branch.subjects')),
                ('sat_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l1', to='branch.subjects')),
                ('sat_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l2', to='branch.subjects')),
                ('sat_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l3', to='branch.subjects')),
                ('sat_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l4', to='branch.subjects')),
                ('sat_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l5', to='branch.subjects')),
                ('sat_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l6', to='branch.subjects')),
                ('sat_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l7', to='branch.subjects')),
                ('sat_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat_l8', to='branch.subjects')),
                ('thurs_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l1', to='branch.subjects')),
                ('thurs_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l2', to='branch.subjects')),
                ('thurs_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l3', to='branch.subjects')),
                ('thurs_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l4', to='branch.subjects')),
                ('thurs_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l5', to='branch.subjects')),
                ('thurs_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l6', to='branch.subjects')),
                ('thurs_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l7', to='branch.subjects')),
                ('thurs_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thurs_l8', to='branch.subjects')),
                ('tues_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l1', to='branch.subjects')),
                ('tues_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l2', to='branch.subjects')),
                ('tues_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l3', to='branch.subjects')),
                ('tues_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l4', to='branch.subjects')),
                ('tues_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l5', to='branch.subjects')),
                ('tues_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l6', to='branch.subjects')),
                ('tues_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l7', to='branch.subjects')),
                ('tues_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tues_l8', to='branch.subjects')),
                ('wed_lec1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l1', to='branch.subjects')),
                ('wed_lec2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l2', to='branch.subjects')),
                ('wed_lec3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l3', to='branch.subjects')),
                ('wed_lec4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l4', to='branch.subjects')),
                ('wed_lec5', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l5', to='branch.subjects')),
                ('wed_lec6', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l6', to='branch.subjects')),
                ('wed_lec7', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l7', to='branch.subjects')),
                ('wed_lec8', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed_l8', to='branch.subjects')),
            ],
            managers=[
                ('branch_obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
