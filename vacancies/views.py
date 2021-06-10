from django.shortcuts import render, redirect
from django.views import View
from vacancies.models import Company, Specialty, Vacancy
from vacancies.forms import MyCompanyCreateForm, MyCompanyForm, MyVacanciesCreateForm, MyVacanciesForm, VacancySendForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# work
def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })
# work
def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
        'vacancies': Vacancy.objects.all()
    })

def vacancy_view(request, vacancy):
    return render(request, 'vacancies/vacancy.html', context={
        'vacancy': Vacancy.objects.all(),
    })
# work
def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.filter(code=specialty),
        'vacancies': Vacancy.objects.all()
    })

def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'specialities': Specialty.objects.all(),
        'vacancies': Vacancy.objects.all()
    })

class mycompany_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-edit.html', context={'form': MyCompanyForm})

    def post(self, request):
        form = MyCompanyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.update()
            return redirect('mycompany')
        return render(request, 'vacancies/company-edit.html', context={'form': form})

class myvacancy_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_edit.html', context={'form': MyVacanciesForm})

    def post(self, request):
        form = MyVacanciesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy_edit.html', context={'form': form})

class mycompany_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('mycompany')
        return render(request, 'vacancies/company-edit.html', context={'form': form})

class myvacancy_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_create.html', context={'form': MyVacanciesCreateForm})

    def post(self, request):
        form = MyVacanciesCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy_create.html', context={'form': form})

class mycompany_letsstart_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('mycompany')
        return render(request, 'vacancies/company-create.html', context={'form': form})

class vacancy_send(View):
    def post(self, request):
        form = VacancySendForm(request.POST)
        if form.is_valid():
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy_send.html', context={'form': form})

class myvacancy_id_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_edit.html', context={'form': MyVacanciesForm})

class MySignupView(CreateView):
   form_class = UserCreationForm
   success_url = 'login'
   template_name = 'vacancies/signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'vacancies/login.html'