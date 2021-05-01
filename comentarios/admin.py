from django.contrib import admin
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'titulo_comentario', 'email', 'comentario', 'post_comentario', 'usario', 'publicado_comentario',
        'data_comentario',)
    list_display_links = ('usario', 'id', 'titulo_comentario',)
    list_editable = ('publicado_comentario',)


admin.site.register(Comentario, ComentarioAdmin)
