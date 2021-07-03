from django.shortcuts import render
from vacancies.models import Company, Specialty



def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })

def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.filter(code=specialty),
    })

def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'companies': Company.objects.filter(title=company),
    })