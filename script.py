import json

import os

import django

from vacancies.models import Company, Specialty, Vacancy

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

if __name__ == '__main__':
    company = Company(
        id='1',
        name='workiro',
        location='Новосибирск',
        logo='https://place-hold.it/100x60',
        description='Разрабатываем мобильные приложения и сервисы для сферы онлайн-обучения.',
        employee_count='10',
    )
    company.save()
    print(company)

# with open('data_specialties.json') as file:
#     specialties_data = json.load(file)
#
# with open('data_vacancies.json') as file:
#     vacancies_data = json.load(file)
