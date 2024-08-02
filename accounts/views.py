from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages

from .forms import UserForm

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print("Success")
            return redirect('/')
        else:
            messages.error(request, 'User not found', fail_silently=False)
            return redirect('/login')

    return render(request, 'login.html')


def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect_to_login(login_url="login", next="home")
