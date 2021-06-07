from django.shortcuts import render, redirect
from django.views import View
from vacancies.models import Company, Specialty, Vacancy
from vacancies.forms import MyCompanyCreateForm, MyCompanyForm, MyVacanciesCreateForm, MyVacanciesForm, VacancySendForm


def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialties': Specialty.objects.all(),
        'vacancies': Vacancy.objects.all()
    })

def vacancy_view(request, vacancy):
    return render(request, 'vacancies/vacancy.html', context={
        'vacancy': Vacancy.objects.filter(specialty_id=vacancy),
    })

def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'specialties': Specialty.objects.filter(code=specialty)
    })

def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'company': Company.objects.filter(title=company),
    })

class mycompany_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-edit.html', context={'form': MyCompanyForm})

    def post(self, request):
        form = MyCompanyForm.request.POST
        if form.is_valid():
            return redirect('company')
        return render(request, 'vacancies/company-edit.html', context={'form': form})


class mycompany_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm.request.POST
        if form.is_valid():
            return redirect('company')
        return render(request, 'vacancies/company-create.html', context={'form': form})

class mycompany_letsstart_view(View):
    def post(self, request):
        form = MyCompanyCreateForm.request.POST
        if form.is_valid():
            return redirect('company')
        return render(request, 'vacancies/company-create.html', context={'form': form})

class myvacancy_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_edit.html', context={'form': MyVacanciesForm})

    def post(self, request):
        form = MyVacanciesForm.request.POST
        if form.is_valid():
            return redirect('vacancy')
        return render(request, 'vacancies/vacancy_edit.html', context={'form': form})

class myvacancy_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_create.html', context={'form': MyVacanciesCreateForm})

    def post(self, request):
        form = MyVacanciesCreateForm.request.POST
        if form.is_valid():
            return redirect('vacancy')
        return render(request, 'vacancies/vacancy_create.html', context={'form': form})

class vacancy_send(View):
    def post(self, request):
        form = VacancySendForm.request.POST
        if form.is_valid():
            return redirect('vacancy')
        return render(request, 'vacancies/vacancy_send.html', context={'form': form})

class myvacancy_id_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy_edit.html', context={'form': MyVacanciesForm})
