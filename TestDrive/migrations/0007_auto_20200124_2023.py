# Generated by Django 3.0.2 on 2020-01-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDrive', '0006_auto_20200124_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='language',
        ),
        migrations.AddField(
            model_name='language',
            name='alpha3',
            field=models.CharField(default='ENG', max_length=3, unique=True, verbose_name='Short language name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(default='English', max_length=30, verbose_name='Language name'),
        ),
    ]
