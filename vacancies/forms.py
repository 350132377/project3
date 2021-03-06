from django import forms

from vacancies.models import Company, Vacancy, Application


class MyCompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'location', 'description', 'employee_count')
        labels = {
            'title': 'Название компании',
            'location': 'География',
            'description': 'Информация о компании',
            'employee_count': 'Количество человек в компании',
        }

class MyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'location', 'description', 'employee_count')
        labels = {
            'title': 'Название компании',
            'location': 'География',
            'description': 'Информация о компании',
            'employee_count': 'Количество человек в компании',
            'owner': 'Владелец компании',
        }

class MyVacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
            'published_at': 'Опубликовано',
        }

class ApplicationSendForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone')
        labels = {
            'written_username': 'Ваше имя',
            'written_phone': 'Номер телефона',
        }
