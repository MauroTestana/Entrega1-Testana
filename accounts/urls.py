from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import login, registrar, editar_usuario, usuario_datos

urlpatterns = [
    path('login/', login  , name='login'),
    path('registrar/', registrar, name='registrar'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('usuario_datos/', usuario_datos, name='usuario_datos'),
    path('editar/', editar_usuario, name='editar_usuario')
]
