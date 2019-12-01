from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User as use


def home(request):

    return render(request, 'index.html')


def my_logout(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        use.objects.create_user(form.data['username'], None, form.data['password1'])
        return redirect('cadastra_user')
    return render(request, "cad_new_user.html", {"form": UserCreationForm() })

# Create your views here.
