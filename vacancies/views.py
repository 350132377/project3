from django.http import Http404
from django.shortcuts import render

from vacancies.models import Company, Specialty, Vacancy


def main_view(request):
    try:
        specialties = Specialty.objects.filter()
        vacancies = Vacancy.objects.all()
        companies = Company.objects.all()
    except KeyError:
        raise Http404
    return render(request, 'vacancies/index.html', context={
        'specialties': specialties,
        'vacancies': vacancies,
        'companies': companies,
    })

def vacancy_view(request):
    try:
        company = Company.objects.get(pk=6)
        vacancy = Vacancy.objects.filter(company_id=6).first()
    except KeyError:
        raise Http404
    return render(request, 'vacancies/vacancy.html', context={
        'company': company,
        'vacancy': vacancy,
    })

def vacancies_view(request):
    try:
        vacancies = Vacancy.objects.all()
    except KeyError:
        raise Http404
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': vacancies,
    })

def vacancies_frontend_view(request):
    try:
        vacancies = Vacancy.objects.filter(specialty_id=10)
    except KeyError:
        raise Http404
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': vacancies,
    })

def company_view(request):
    try:
        company = Company.objects.get(pk=6)
        vacancies = Vacancy.objects.filter(company_id=6)
    except KeyError:
        raise Http404
    return render(request, 'vacancies/company.html', context={
        'company': company,
        'vacancies': vacancies,
    })

def custom_handler404(request, exception=None, template_name='vacancies/errors/404.html'):
    return render(request, template_name)

def custom_handler500(request, template_name='vacancies/errors/500.html'):
    return render(request, template_name)
