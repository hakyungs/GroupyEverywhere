# Generated by Django 2.2.5 on 2019-09-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190914_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
