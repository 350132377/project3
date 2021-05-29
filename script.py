import json

import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'baza_vakansiy_it.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy


with open('data_companies.json') as file:
    companies_data = json.load(file)
    for company_data in companies_data:
        company = Company.objects.create(
            id=company_data['id'],
            name=company_data['name'],
            location=company_data['location'],
            logo=company_data['logo'],
            description=company_data['description'],
            employee_count=company_data['employee_count'],
        )

with open('data_specialties.json') as file:
    specialties_data = json.load(file)


with open('data_vacancies.json') as file:
    vacancies_data = json.load(file)
