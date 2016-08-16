# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


def load_stores_from_sql():
    from OlimpiColombia.settings import BASE_DIR
    import os
    sql_statements = open(os.path.join(BASE_DIR,'OlimpiColombiaSite/sql/deporte.sql'), 'r').read()
    return sql_statements

class Migration(migrations.Migration):

    dependencies = [
        ('OlimpiColombiaSite', '0002_auto_20160815_2048'),
    ]

    operations = [
        migrations.RunSQL(load_stores_from_sql()),
    ]