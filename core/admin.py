from django.contrib import admin
from .models import Foto, Categorias, SobreMim

class FotoAdmin(admin.ModelAdmin):
    list_display = ["foto", "categoria"]

admin.site.register(Foto, FotoAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["nome"]

admin.site.register(Categorias, CategoriasAdmin)

class SobreMimAdmin(admin.ModelAdmin):
    list_display = ["foto", 'descricao']

admin.site.register(SobreMim, SobreMimAdmin)
