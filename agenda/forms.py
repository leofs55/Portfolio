# flake8: noqa
from django.core.exceptions import ValidationError
from django import forms
from agenda.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation# type: ignore


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
        ),
        required=False
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
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Este email não pode ser utilizado duas vezes.',
                    code='invalid'
                )
            )
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
    def clean(self):
        password1, password2 = self.cleaned_data.get('password1'),self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não coencidem.')
                )
        return super().clean()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if self.instance.email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Este email não pode ser utilizado duas vezes.',
                        code='invalid'
                    )
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1