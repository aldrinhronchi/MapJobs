from django.urls import path
from .views import home, my_logout, register_user


urlpatterns = [

    path('', home, name="home"),
    path('acount/new/', register_user, name='register_new'),
    path('logout/', my_logout, name="logout"),

    ]