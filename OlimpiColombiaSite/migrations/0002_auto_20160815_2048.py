# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OlimpiColombiaSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=1, max_digits=4)),
                ('estatura', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fotografia', models.CharField(max_length=1000)),
                ('video_destacado', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('rival', models.CharField(blank=True, max_length=100)),
                ('resultado', models.CharField(max_length=100)),
                ('video_destacado', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('medalla', models.CharField(blank=True, max_length=20)),
                ('entrenador', models.CharField(max_length=200)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OlimpiColombiaSite.Atleta')),
            ],
        ),
        migrations.AddField(
            model_name='deporte',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='modalidad',
            name='deporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OlimpiColombiaSite.Deporte'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='modalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OlimpiColombiaSite.Modalidad'),
        ),
    ]
