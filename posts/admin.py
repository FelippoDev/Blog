from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data_post', 'categoria', 'publicado_post',)
    list_editable = ('publicado_post',)
    list_display_links = ('id', 'titulo',)


admin.site.register(Post, PostAdmin)
