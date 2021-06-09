from django import forms
from vacancies.models import Company, Vacancy, Application, User


class MyCompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'location', 'logo', 'description', 'employee_count')

class MyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'location', 'logo', 'description', 'employee_count', 'owner')

class MyVacanciesCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max')

class MyVacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')

class VacancySendForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'vacancy', 'user')
