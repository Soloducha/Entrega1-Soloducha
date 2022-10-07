from django.db import models

class Veterinario(models.Model):
    class Meta:
        verbose_name_plural = "Veterinarios"
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula = models.IntegerField()

    def __str__(self):
        return self.apellido


class Animal(models.Model):
    class Meta:
        verbose_name_plural = "Animales"

    nombre = models.CharField(max_length=30)
    dueño_nombre = models.CharField(max_length=40)
    dueño_apellido = models.CharField(max_length=40)
    raza = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    class Meta:
        verbose_name_plural = "Clientes"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.apellido