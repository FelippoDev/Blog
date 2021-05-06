from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo = models.TextField(verbose_name='Conteúdo')
    imagem = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, verbose_name='Imagens')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True,
                                  verbose_name='Categorias')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicação')
    excerto = models.TextField(verbose_name='Excerto', null=True)

    def __str__(self):
        return self.titulo
