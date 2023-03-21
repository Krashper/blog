from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        widget = {
            'username': TextInput(attrs={
                'placeholder': 'Логин'
            }),
            'password': TextInput(attrs={
                'placeholder': 'Пароль'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Email'
            }),
        }