from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from django.contrib import messages
from comentarios.forms import FormComentario
from comentarios.models import Comentario


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            n_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )

        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        if termo is None or not termo:
            return qs
        qs = qs.filter(
            Q(titulo__icontains=termo) | Q(conteudo__icontains=termo) | Q(excerto__icontains=termo) |
            Q(autor__first_name__iexact=termo)
        )

        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria__nome_cat__iexact=categoria)
        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario=True,
                                                post_comentario=post.id)

        contexto['comentarios'] = comentarios
        print(contexto['comentarios'])
        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário enviado com sucesso.')
        return redirect('post_detalhes', pk=post.id)
