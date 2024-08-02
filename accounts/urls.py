from django.urls import path
from .views import (
    login_view,
    logout_view, 
    register, follow_user, unfollow_user, profile
)
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name='logout'),
    path('follow/<str:username>/', follow_user, name='follow_user'),
    path('unfollow/<str:username>/', unfollow_user, name='unfollow_user'),
    path('profile/<str:username>/', profile, name='profile'),
]
