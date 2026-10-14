from django.contrib import admin
from shop.models import Equipo, Arriendo

# Register your models here.
admin.site.register(Equipo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ['equipo', 'fecha_inicio', 'fecha_fin', 'cliente', 'precio_formateado']
    list_filter = ['equipo', 'fecha_inicio', 'fecha_fin']
    search_fields = ['cliente']



admin.site.register(Arriendo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'stock', 'url_imagen']
    search_fields = ['nombre']