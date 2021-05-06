from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from posts.models import Post


class Comentario(models.Model):
    titulo_comentario = models.CharField(max_length=255, verbose_name='Título')
    email = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Nome Post')
    usario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicação')

    def __str__(self):
        return self.titulo_comentario
