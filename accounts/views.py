from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm


class MySignupView(CreateView):
   form_class = UserCreationForm
   success_url = 'login'
   template_name = 'accounts/signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
