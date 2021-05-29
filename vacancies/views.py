from django.shortcuts import render

from vacancies.models import Company, Specialty, Vacancy

def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'companies': Company.objects.all(),
        'specialties': Specialty.objects.all(),
    })

def vacancy_view(request):
    return render(request, 'vacancies/vacancy.html')

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': Vacancy.objects.all(),
    })

def vacancies_frontend_view(request):
    return render(request, 'vacancies/vacancy.html')

def company_view(request):
    return render(request, 'vacancies/company.html')