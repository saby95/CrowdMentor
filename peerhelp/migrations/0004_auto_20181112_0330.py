# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peerhelp', '0003_auto_20181112_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answervotes',
            name='answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='peerhelp.Answer'),
        ),
        migrations.AlterField(
            model_name='questionvotes',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='peerhelp.Question'),
        ),
    ]
