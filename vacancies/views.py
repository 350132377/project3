from django.shortcuts import render

from vacancies.models import Company, Specialty, Vacancy

def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'companies': Company.objects.all(),
        'specialties': Specialty.objects.all(),
    })

def vacancy_view(request):
    return render(request, 'vacancies/vacancy.html', context={
        'company': Company.objects.get(pk=6),
        'vacancy': Vacancy.objects.filter(company_id=6).first(),
    })

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': Vacancy.objects.all(),
    })

def vacancies_frontend_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'vacancies': Vacancy.objects.filter(specialty_id=10),
    })

def company_view(request):
    return render(request, 'vacancies/company.html', context={
        'company': Company.objects.get(pk=6),
        'vacancies': Vacancy.objects.filter(company_id=6),
    })

def custom_handler404(request, exception=None, template_name='tours/errors/404.html'):
    return render(request, template_name)

def custom_handler500(request, template_name='tours/errors/505.html'):
    return render(request, template_name)