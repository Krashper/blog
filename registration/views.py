from django.shortcuts import render, redirect
from .forms import UsersForm

# Create your views here.
def registration(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
        else: 
            error = 'Форма была неверной'
    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration.html', data)

