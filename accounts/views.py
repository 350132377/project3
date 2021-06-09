from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import MySignupView, MyLoginView


class login_view(View):
    def get(self, request):
        return render(request, 'vacancies/login.html', context={'form': MyLoginView})

    def post(self, request):
        form = MyLoginView.request.POST
        if form.is_valid():
            return redirect('login')
        return render(request, 'accounts/login.html', context={'form': form})

class signup_view(View):
    def get(self, request):
        return render(request, 'accounts/signup.html', context={'form': MySignupView})

    def post(self, request):
        form = MySignupView.request.POST
        if form.is_valid():
            return redirect('signup')
        return render(request, 'accounts/signup.html', context={'form': form})
