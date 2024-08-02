from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.template.loader import render_to_string

from .models import Follow, Account

from .forms import UserForm

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
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


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(Account, username=username)
    if request.user != user_to_follow:
        Follow.objects.get_or_create(
            follower=request.user, followed=user_to_follow)
    if request.htmx:
        followers = Follow.objects.filter(followed=user_to_follow)
        html = render_to_string('partials/follow_button.html', {
            'profile_user': user_to_follow,
            'is_following': True,
            'followers_count': followers.count()
        })
        return HttpResponse(html)
    return redirect('profile', username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(Account, username=username)
    Follow.objects.filter(follower=request.user,
                          followed=user_to_unfollow).delete()
    if request.htmx:
        followers = Follow.objects.filter(followed=user_to_unfollow)
        html = render_to_string('partials/follow_button.html', {
            'profile_user': user_to_unfollow,
            'is_following': False,
            'followers_count': followers.count()
        })
        return HttpResponse(html)
    return redirect('profile', username=username)


@login_required
def profile(request, username):
    user = get_object_or_404(Account, username=username)
    is_following = Follow.objects.filter(
        follower=request.user, followed=user).exists()
    followers = Follow.objects.filter(followed=user)
    following = Follow.objects.filter(follower=user)
    return render(request, 'profile.html', {
        'profile_user': user,
        'is_following': is_following,
        'followers': followers,
        'following': following,
    })

