from django.db import models


class Puesto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.IntegerField(blank=False, null=False, default=0)


    def __str__(self):
        return self.nombre

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.BigIntegerField()
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    descripcion_corta = models.TextField(blank=True, null=True)
    mostrar_en_inicio =  models.BooleanField(default=False) 

    imagen = models.ImageField(upload_to='images/empleados', blank=True, null=True)


    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    # https://www.freepik.com/icon/
    imagen = models.ImageField(upload_to='images/servicios', blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Partner(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='images/servicios', blank=True, null=True)
    sitio_web = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.nombre

