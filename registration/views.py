from django.shortcuts import render, redirect
from .forms import UsersForm
from django.contrib.auth.models import User


# Create your views here.
def registration(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            email = email.strip()
            if User.objects.filter(email=email).exists():
                error = 'A user with such an email already exists'
            else:
                send_user_data(form.cleaned_data['username'], email, form.cleaned_data['password'])
        else:
            error = 'Форма была неверной'
    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration.html', data)

def send_user_data(username, email, password):
    user = User(username=username, email=email, password=password)
    user.save()
