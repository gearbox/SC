# Generated by Django 3.0.2 on 2020-01-24 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TestDrive', '0009_auto_20200124_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scpoint',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date on which the SpeedCam was added'),
        ),
    ]
