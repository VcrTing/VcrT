# Generated by Django 2.0.5 on 2018-08-08 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kouzactrl',
            name='create_date',
        ),
        migrations.AddField(
            model_name='kouza',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 980389, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='kouzactrl',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 8, 9, 13, 18, 979390, tzinfo=utc), verbose_name='最近更新时间'),
        ),
    ]
