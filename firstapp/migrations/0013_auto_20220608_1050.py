# Generated by Django 3.2.7 on 2022-06-08 05:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20220608_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoholhabits',
            name='time_active',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fatigue',
            name='fatigue',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='geneticrisk',
            name='number_of_relatives',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
