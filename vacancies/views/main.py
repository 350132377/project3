from django.shortcuts import render
from vacancies.models import Company, Specialty, Vacancy
from django.shortcuts import get_object_or_404


def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
    })

def vacancy_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'vacancies/vacancy.html', context={
        'vacancy': vacancy,
        'company': company,
    })

def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.filter(code=specialty),
    })

def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'companies': Company.objects.filter(title=company),
    })