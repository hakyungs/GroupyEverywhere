# Generated by Django 2.2.5 on 2019-09-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_event_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.CharField(max_length=30),
        ),
    ]