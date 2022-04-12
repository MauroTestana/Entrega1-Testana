from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
#from ckeditor.fields import RichTextField 

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=20) 
    post  = RichTextField(blank=True, null=True)
    autor = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='pic', blank=True, null=True, )
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.titulo}, Autor:{self.autor}"
    
    

    
    

      






