# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 21:33
from __future__ import unicode_literals

from django.db import migrations


def load_stores_from_sql():
    from OlimpiColombia.settings import BASE_DIR
    import os
    sql_statements = open(os.path.join(BASE_DIR, 'OlimpiColombiaSite/sql/atleta.sql'),  encoding="utf8").read()
    return sql_statements


class Migration(migrations.Migration):
    dependencies = [
        ('OlimpiColombiaSite', '0004_initial_data_modalidad'),
    ]

    operations = [
        migrations.RunSQL(load_stores_from_sql()),
    ]
