


from django.contrib import admin
from.models import User, PrestadorServico, TypeService, Qualificacao, Avaliacao, FormsPayment, Cities, States
# Register your models here.

admin.site.register(User)
admin.site.register(PrestadorServico)
admin.site.register(TypeService)
admin.site.register(Cities)
admin.site.register(Avaliacao)
admin.site.register(Qualificacao)
admin.site.register(FormsPayment)
admin.site.register(States)

