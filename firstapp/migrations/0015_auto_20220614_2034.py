# Generated by Django 3.2.7 on 2022-06-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_auto_20220608_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obesity',
            name='bmi',
        ),
        migrations.AlterField(
            model_name='smokinghabits',
            name='current_smoking_habits',
            field=models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive'), ('Past Smoker', 'Past Smoker'), ('Non-Smoker', 'Non-Smoker')], max_length=20),
        ),
    ]