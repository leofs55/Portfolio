# flake8:noqa
# type:ignore
from django.core.exceptions import ValidationError
from django import forms
from agenda.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self):
        cleaned_data = self.cleaned_data 

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )
        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )
        return super().clean()
