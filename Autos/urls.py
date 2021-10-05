from django.urls import path, include
from . import views

urlpatterns = [
    path('registro_autos', views.registro_autos, name='registro_autos'),
    path('lista_autos', views.lista_autos, name="lista_autos"),
    path('registro_motos', views.registro_moto, name='registro_motos'),
    path('lista_motos', views.lista_moto, name="lista_motos"),
    path('editar_auto/<int:id>/', views.editarAuto, name= 'editar_auto'),
    path('eliminar_auto/<int:id>/', views.eliminarAuto, name= 'eliminar_auto'),
    path('editar_moto/<int:id>/', views.editarMoto, name= 'editar_moto'),
    path('eliminar_moto/<int:id>/', views.eliminarMoto, name= 'eliminar_moto'),
]