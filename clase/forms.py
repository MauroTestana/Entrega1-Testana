from django import forms
from ckeditor.fields import RichTextFormField


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class BusquedaCurso(forms.Form):
    partial_curso = forms.CharField(label='Buscador',max_length=20)
    
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = RichTextFormField(required=False)
    email = forms.EmailField()
    pic = forms.ImageField(required=False)
