from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    publicado_post = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
