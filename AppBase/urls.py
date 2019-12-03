
from django.urls import path
from .views import CreateUser
from .views import user_update
from .views import prestador_list
from .views import prestador_delete
from .views import prestador_update
from .views import avaliacao_new
from .views import avaliacao_list
from .views import avaliacao_update
from .views import avaliacao_delete
from .views import qualificacao_new
from .views import qualificacao_list
from .views import qualificacao_update
from .views import qualificacao_delete
from .models import User
from .views import perfil, prestador_new, details

urlpatterns = [

    path('user/new/', CreateUser.as_view(model=User), name="cadastra_user"),
    path('prest/new/', prestador_new, name="prestador_new"),
    path('user/list/details/<int:id>', details, name="details"),
    path('user/list/', perfil, name="profile"),
    path('prest/list/', prestador_list, name="result"),


    # implementar
    path('prest/list/qual/', qualificacao_list, name="qualificacao_list"),
    path('prest/aval/list/', avaliacao_list, name="avaliacao_list"),
    path('prest/qual/list/', qualificacao_list, name="qualificacao_list"),
    path('prest/aval/new/', avaliacao_new, name="avaliacao_new"),
    path('prest/qual/new/', qualificacao_new, name="qualificacao_new"),
    path('update/<int:id>/', user_update, name="user_update"),
    path('prest/update/<int:id>/', prestador_update, name="prestador_update"),
    path('prest/aval/update/<int:id>/', avaliacao_update, name="avaliacao_update"),
    path('prest/qual/update/<int:id>/', qualificacao_update, name="qualificacao_update"),

    path('prest/delete/<int:id>/', prestador_delete, name="prestador_delete"),
    path('prest/aval/delete/<int:id>/', avaliacao_delete, name="avaliacao_delete"),
    path('prest/qual/delete/<int:id>/', qualificacao_delete, name="qualificacao_delete"),

]