from django.urls import path, include
from . import views

urlpatterns = [
   path('registro_clientes', views.registro_clientes, name="registrar_clientes" ),
   path('lista_clientes', views.lista_clientes, name="lista_clientes"),
   path('editar_cliente/<int:id>/', views.editar_cliente, name= 'editar_cliente'),
   path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name= 'eliminar_cliente'),
    
]