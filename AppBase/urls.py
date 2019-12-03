
from django.urls import path
from .views import CreateUser, pay_delete, pay_list, pay_new, auxs, est_update, est_delete, est_new, est_list, \
    city_update, city_delete, city_new, city_list, active_list, active_new, active_update, active_delete
from .views import pay_update
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

    path('update/pay/<int:id>/', pay_update, name="pay_updates"),
    path('pay/delete/<int:id>/', pay_delete, name="delete_pay"),
    path('pay/new/', pay_new, name="pay_new"),
    path('pay/list/', pay_list, name="pay_lists"),

    path('aux/', auxs, name="auxiliar"),

    path('update/est/<int:id>/', est_update, name="est_updates"),
    path('est/delete/<int:id>/', est_delete, name="delete_est"),
    path('est/new/', est_new, name="est_new"),
    path('est/list/', est_list, name="est_lists"),

    path('update/cyty/<int:id>/', city_update, name="city_updates"),
    path('city/delete/<int:id>/', city_delete, name="delete_city"),
    path('city/new/', city_new, name="city_new"),
    path('city/list/', city_list, name="city_lists"),

    path('update/active/<int:id>/', active_update, name="active_updates"),
    path('active/delete/<int:id>/', active_delete, name="delete_active"),
    path('active/new/', active_new, name="active_new"),
    path('active/list/', active_list, name="active_lists"),


    # implementar
    path('prest/list/qual/', qualificacao_list, name="qualificacao_list"),
    path('prest/aval/list/', avaliacao_list, name="avaliacao_list"),
    path('prest/qual/list/', qualificacao_list, name="qualificacao_list"),
    path('prest/aval/new/', avaliacao_new, name="avaliacao_new"),
    path('prest/qual/new/', qualificacao_new, name="qualificacao_new"),


    path('prest/update/<int:id>/', prestador_update, name="prestador_update"),
    path('prest/aval/update/<int:id>/', avaliacao_update, name="avaliacao_update"),
    path('prest/qual/update/<int:id>/', qualificacao_update, name="qualificacao_update"),

    path('prest/delete/<int:id>/', prestador_delete, name="prestador_delete"),
    path('prest/aval/delete/<int:id>/', avaliacao_delete, name="avaliacao_delete"),
    path('prest/qual/delete/<int:id>/', qualificacao_delete, name="qualificacao_delete"),

]