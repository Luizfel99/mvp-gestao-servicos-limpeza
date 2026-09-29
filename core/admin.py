from django.contrib import admin

from .models import Cliente, Propriedade, Profissional, Servico


admin.site.register(Cliente)
admin.site.register(Propriedade)
admin.site.register(Profissional)
admin.site.register(Servico)
