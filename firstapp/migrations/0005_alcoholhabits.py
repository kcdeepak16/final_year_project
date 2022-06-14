# Generated by Django 3.2.7 on 2022-06-07 15:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0004_auto_20220607_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlcoholHabits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alcohol_habits', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Occassionally', 'Occassionally'), ('Non Drinker', 'Non Drinker')], max_length=20)),
                ('time_active', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
