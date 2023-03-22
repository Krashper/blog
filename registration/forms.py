from django.contrib.auth.models import User
from django.forms import TextInput, EmailField, forms, CharField, EmailInput, PasswordInput
class UsersForm(forms.Form):
    first_name = CharField(
        min_length = 2,
        widget = TextInput(
            attrs = {
                'placeholder': 'First name'
            }
        )
    )
    last_name = CharField(
        min_length = 2,
        widget = TextInput(
            attrs = {
                'placeholder': 'Last name'
            }
        )
    )
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
        min_length=8,
        widget = PasswordInput(
            attrs = {
                'placeholder': 'Password'
            }
        )
    )
    