from django import forms
from vacancies.models import Company, Specialty, Vacancy, Application


class MyCompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('title', 'location', 'logo', 'description', 'employee_count', 'owner')