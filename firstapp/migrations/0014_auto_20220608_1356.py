# Generated by Django 3.2.7 on 2022-06-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_auto_20220608_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='obesity',
            name='bmi',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='obesity',
            name='weight',
            field=models.IntegerField(),
        ),
    ]