# Generated by Django 2.2.5 on 2019-09-14 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0004_auto_20190914_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('andrewID', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=10)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('size', models.IntegerField()),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_leader', to='catalog.User')),
                ('members', models.ManyToManyField(related_name='members', to='catalog.User')),
            ],
        ),
    ]
