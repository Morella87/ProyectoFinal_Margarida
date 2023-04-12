from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Texto(models.Model):
    tituloLibro = models.CharField(max_length=80)
    autor = models.CharField(max_length=40)
    edicion = models.IntegerField(null=True)
    genero = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40, blank=True)
    disponible = models.CharField(max_length=10)
    tapaLibro = models.ImageField(default=None, null=True, blank=True, upload_to='portada/')

    def __str__(self):
        return f"Titulo: {self.tituloLibro} - Autor: {self.autor} - Edición: {self.edicion} - Genero: {self.genero} - Editorial: {self.editorial} - Disponible: {self.disponible} - Tapa Libro: {self.tapaLibro}"

class Propietario(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    telefono= models.IntegerField()
    email= models.EmailField()
    tituloLibro = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} - Email: {self.email} - Titulo: {self.tituloLibro}"

class Creador(models.Model):
    nombreaut= models.CharField(max_length=20)
    apellidoaut= models.CharField(max_length=40, null=True, blank=True)
    tituloLibro = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombreaut} - Apellido: {self.apellidoaut} - Titulo: {self.tituloLibro}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"