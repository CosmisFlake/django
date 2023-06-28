from django.contrib import admin
from .models import *
# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created_at','updated_at')
    list_display = ('id','marca')
    ordering = ['marca']

class JoyeriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('idJoyeria','name','marca','tipo','value','stock')
    ordering = ['name','marca']

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Joyeria, JoyeriaAdmin)