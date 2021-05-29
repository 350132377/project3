import json
import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

with open('data_companies.json') as file:
    companies_data = json.load(file)

with open('data_specialties.json') as file:
    specialties_data = json.load(file)

with open('data_vacancies.json') as file:
    vacancies_data = json.load(file)