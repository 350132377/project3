from django.shortcuts import render

from baza_vakansiy_it.vacancies.data import jobs, companies, specialties


def main_view(request):
    return render(request, 'vacancies/index.html')

def vacancy_view(request):
    return render(request, 'vacancies/vacancy.html')

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html')

def vacancies_frontend_view(request):
    return render(request, 'vacancies/vacancy.html')

def company_view(request):
    return render(request, 'vacancies/company.html')