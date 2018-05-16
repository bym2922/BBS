# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('icon', models.ImageField(upload_to='')),
                ('sex', models.CharField(choices=[('F', '男'), ('M', '女'), ('U', '保密')], max_length=8)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
