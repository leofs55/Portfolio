# flake8: noqa
from django.core.exceptions import ValidationError
from django import forms
from agenda.models import Contact
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'classe-a classe-b',
    #             'placeholder': 'Aqui veio o init',
    #         }
    #     ),
    #     help_text='Texto de ajuda para o usuario.'
    # )
    pictures = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'pictures'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name, last_name = cleaned_data.get('first_name'), cleaned_data.get('last_name')# type: ignore
        
        if first_name == last_name:
            msg = ValidationError(
                    'Estes campos não podem ser iguais!', code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC',
                    code='invalid'
                )
            )
        return first_name

class RegisterForm(UserCreationForm):
    ...
