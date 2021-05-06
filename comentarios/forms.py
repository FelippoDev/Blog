from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def cleanC(self):
        data = self.cleaned_data


    class Meta:
        model = Comentario
        fields = ('usario', 'email', 'titulo_comentario', 'comentario',)
