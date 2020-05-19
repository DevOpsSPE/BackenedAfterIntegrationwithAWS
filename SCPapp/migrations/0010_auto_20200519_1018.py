# Generated by Django 3.0.6 on 2020-05-19 10:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SCPapp', '0009_auto_20200519_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentspyq',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='commentspyq',
            name='object_id',
        ),
        migrations.AddField(
            model_name='commentspyq',
            name='pyq',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SCPapp.File'),
        ),
        migrations.AddField(
            model_name='interview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]