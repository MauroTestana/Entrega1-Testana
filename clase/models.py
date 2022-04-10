from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
#from ckeditor.fields import RichTextField 

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=20) 
    apellido  = RichTextField(blank=True, null=True)
    email = models.EmailField()
    pic = models.ImageField(upload_to='pic', blank=True, null=True, )
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.nombre} {self.email}"
    
    

    
    
class Curso(models.Model):
    nombre = models.CharField(max_length=20) 
    camada  = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"
      






