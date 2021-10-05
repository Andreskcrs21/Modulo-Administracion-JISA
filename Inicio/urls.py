from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   # path("", views.bienvenida, name='bienvenida'),
   path("", LoginView.as_view(template_name='login/login.html'), name="login"),
   path("registro/", views.registro, name='registro'),
   path("inicio/", views.inicio, name='inicio'),
   # path("login/", LoginView.as_view(template_name='login/login.html'), name="login"),
   path("logout/", LogoutView.as_view(template_name='login/login.html'), name="logout"),

    
]