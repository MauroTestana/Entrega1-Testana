from django.db import models
#from ckeditor.fields import RichTextField 

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido  = models.CharField(max_length=30)
    email = models.EmailField()
    pic = models.ImageField(upload_to='pic', blank=True, null=True, )
#    folleto = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.pic}"
    
    
#class Profesor(models.Model):
#    nombre = models.CharField(max_length=20) 
#    apellido  = models.CharField(max_length=30)
#    email = models.EmailField()
#    profesion = models.CharField(max_length=30)
    
    
class Curso(models.Model):
    nombre = models.CharField(max_length=20) 
    camada  = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"
      

#class Entegrables(models.Model):
#    nombre = models.CharField(max_length=20) 
#    FechaDeEntrega  = models.DateTimeField()
#   entregado = models.BooleanField() 





