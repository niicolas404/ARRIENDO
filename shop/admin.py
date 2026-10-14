from django.contrib import admin
from .models import Equipo, Arriendo


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ['equipo', 'fecha_inicio', 'fecha_fin', 'cliente', 'precio_formateado']
    list_filter = ['equipo', 'fecha_inicio', 'fecha_fin']
    search_fields = ['cliente']


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'stock', 'url_imagen']
    search_fields = ['nombre']