from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Imagen(models.Model):
    url = models.CharField(max_length=1000)

class Deporte(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=150, blank=True)
	imagen =  models.CharField(max_length=1000)

class Atleta(models.Model):
    nombres = models.CharField(max_length=200)
    lugar_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=4, decimal_places=1)
    estatura = models.DecimalField(max_digits=4, decimal_places=1)
    fotografia = models.CharField(max_length=1000)
    video_destacado = models.CharField(max_length=1000, blank=True)

class Modalidad(models.Model):
	nombre = models.CharField(max_length=50)
	medalla = models.CharField(max_length=20, blank=True)
	entrenador = models.CharField(max_length=200)
	deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
	atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

class Competencia(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    rival = models.CharField(max_length=100, blank=True)
    resultado = models.CharField(max_length=100)
    video_destacado = models.CharField(max_length=1000, blank=True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre