# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpiColombiaSite', '0005_initial_data_atleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='competencia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='momento_destacado', to='OlimpiColombiaSite.Competencia'),
        ),
    ]
