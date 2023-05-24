from django.contrib import admin
from .models import Foto, Categorias, SobreMim,CamposAlteraveis

class FotoAdmin(admin.ModelAdmin):
    list_display = ["pk", "foto", "categoria", "destaque"]

admin.site.register(Foto, FotoAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["nome"]

admin.site.register(Categorias, CategoriasAdmin)

class SobreMimAdmin(admin.ModelAdmin):
    list_display = ["foto", 'descricao']

admin.site.register(SobreMim, SobreMimAdmin)

class CamposAlteraveisAdmin(admin.ModelAdmin):
    list_display = ["pk", "nome_campo", 'texto_campo']

admin.site.register(CamposAlteraveis, CamposAlteraveisAdmin)
