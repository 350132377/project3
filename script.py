import json

import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'baza_vakansiy_it.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy


# работает
# with open('data_companies.json', encoding='utf-8') as file:
#     companies_data = json.load(file)
#     for company_data in companies_data:
#         company = Company.objects.create(
#             id=company_data['id'],
#             name=company_data['name'],
#             location=company_data['location'],
#             logo=company_data['logo'],
#             description=company_data['description'],
#             employee_count=company_data['employee_count'],
#         )

# работает
# with open('data_specialties.json', encoding='utf-8') as file:
#     specialties_data = json.load(file)
#     for specialty_data in specialties_data:
#         specialty_data = Specialty.objects.create(
#             code=specialty_data['code'],
#             title=specialty_data['title'],
#             picture=specialty_data['picture'],
#         )

with open('data_vacancies.json', encoding='utf-8') as file:
    vacancies_data = json.load(file)
    for vacancy_data in vacancies_data:
        vacancy_data = Vacancy.objects.create(
            id=vacancy_data['id'],
            title=vacancy_data['title'],
            skills=vacancy_data['skills'],
            description=vacancy_data['description'],
            salary_min=vacancy_data['salary_min'],
            salary_max=vacancy_data['salary_max'],
            published_at=vacancy_data['published_at'],
            company=Company.objects.get(id=vacancy_data['company']),
            specialty=Specialty.objects.get(code=vacancy_data['specialty']),
        )
