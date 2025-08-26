from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    dueno = models.CharField(max_length=100)

    def __str__(self):
        return self.patente