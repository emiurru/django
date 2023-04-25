from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=64) #charfield es para espicificar que el dato es str
    comision =  models.IntegerField() # equivalente de int

class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    dni = models.CharField(max_length=20) 
    telefono = models.CharField(max_length=32) # es buena practica poner en str
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    dni = models.CharField(max_length=20) 
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField() # para no tener que poner un maximo

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)

