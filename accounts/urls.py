from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import MyLoginView, MySignupView

urlpatterns = [
    # авторизация, регистрация
    path('register/', MySignupView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]