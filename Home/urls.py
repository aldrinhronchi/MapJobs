from django.urls import path
from .views import home, my_logout, cadastrar_usuario


urlpatterns = [

    path('', home, name="home"),
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logout/', my_logout, name="logout"),

    ]