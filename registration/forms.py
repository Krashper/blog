from django.contrib.auth.models import User
from django.forms import TextInput, EmailField, forms, CharField, EmailInput, PasswordInput
class UsersForm(forms.Form):
    username = CharField(
        min_length = 2,
        widget = TextInput(
            attrs = {
                'placeholder': 'Username'
            }
        )
    )
    email = EmailField(
        widget = EmailInput(
            attrs = {
                'placeholder': 'Email',
            }
        )
    )
    password = CharField(
        min_length=4,
        widget = PasswordInput(
            attrs = {
                'placeholder': 'password'
            }
        )
    )