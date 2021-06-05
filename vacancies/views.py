from django.shortcuts import get_object_or_404
from django.shortcuts import render

from vacancies.models import Company, Specialty, Vacancy



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
