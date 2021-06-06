from django.shortcuts import render, redirect
from django.views import View
from vacancies.models import Company, Specialty, Vacancy
from vacancies.forms import MyCompanyCreateForm, MyCompanyForm, MyVacanciesCreateForm, MyVacanciesForm


def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': Vacancy.objects.all()
    })

def vacancy_view(request, company, vacancy):
    return render(request, 'vacancies/vacancy.html', context={
        'company': Company.objects.filter(title=company),
        'vacancy': Vacancy.objects.filter(specialty=vacancy),
    })

def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'speciality': Specialty.objects.filter(code=specialty)
    })

def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'company': Company.objects.filter(title=company),
    })

def mycompany_view(View):
    def get(self, request):
        return render(request, 'vacancies/company_edit.html', context={'form': MyCompanyForm})

    def post(self, request):
        form = MyCompanyCreateForm.request.POST
        if form.is_valid():
            return redirect('company')
        return render(request, 'vacancies/company_edit.html', context={'form': form})


def mycompany_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/company_create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm.request.POST
        if form.is_valid():
            return redirect('company')
        return render(request, 'vacancies/company_create.html', context={'form': form})

def mycompany_letsstart_view(request):
    return render(request)