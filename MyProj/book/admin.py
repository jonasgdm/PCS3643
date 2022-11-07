from django.contrib import admin

from book.models import Voo

class VooAdmin(admin.ModelAdmin):
    list_display = ('idVoo', 'companhiaAerea', 'origem', 'destino', 'statusVoo')

admin.site.register(Voo, VooAdmin)

# Register your models here.
