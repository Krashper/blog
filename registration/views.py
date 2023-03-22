from django.shortcuts import render, redirect
from .forms import UsersForm
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def registration(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            email = email.strip()
            username = form.cleaned_data.get('username', None)
            username = username.strip()
            if User.objects.filter(username=username).exists():
                error = 'A user with such an username already exists'
            elif User.objects.filter(email=email).exists():
                error = 'A user with such an email already exists'
            else:
                send_user_data(form.cleaned_data['first_name'], form.cleaned_data['last_name'], username, email, form.cleaned_data['password'])
    else:
        error = 'The form was incorrect'

    form = UsersForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'registration/registration.html', data)

def send_user_data(first_name, last_name, username, email, password):
    user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
    user.save()
    return redirect('login')
