from django.urls import path
from accounts.forms import MySignupView, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/signup/', MySignupView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]