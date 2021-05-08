from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')

        if len(nome) < 3:
            self.add_error(
                'nome_comentario',
                'O nome precisa de no mínimo 3 caracteres.'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email', 'titulo_comentario', 'comentario',)
