from distutils.command.upload import upload
from django.db import models
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    mensaje = models.CharField(max_length=500)
    
    def __str__ (self):
        return self.nombre
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    marca= models.CharField(max_length=30)
    tipo= models.CharField(max_length=100)
    animal= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre