from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from posts.models import Post


class Comentario(models.Model):
    titulo_comentario = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
