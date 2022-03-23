from django.urls import path
from .views import index, plantilla, login

urlpatterns = [
    path('', index, name='index'),
    path('plantilla/', plantilla, name='plantilla'),
    path('login/', login  , name='login')
]
