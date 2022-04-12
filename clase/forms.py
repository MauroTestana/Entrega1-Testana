from django import forms
from ckeditor.fields import RichTextFormField


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class BusquedaPost(forms.Form):
    partial_post = forms.CharField(label='Buscador',max_length=20)
    
    
class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=20)
    post = RichTextFormField(required=False)
    autor = forms.CharField(max_length=20)
    pic = forms.ImageField(required=False)
