from django.shortcuts import render, redirect
from vacancies.models import Vacancy
from django.shortcuts import get_object_or_404
from django.views import View
from vacancies.forms import VacancySendForm, MyVacanciesForm


def vacancy_send(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/sent.html', context={
        'vacancy': vacancy,
    })

# work список
def my_company_vacancies(request):
    return render(request, 'vacancies/vacancy-list.html')
# work пустая форма
def my_company_vacancies_create(request):
    return render(request, 'vacancies/vacancy-edit.html')
# work заполненная форма
def my_company_vacancy_id(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/vacancy-edit.html', context={
        'vacancy': vacancy,
    })

# Создайте форму отправки отклика на вакансию на основе модели Application
# не появляется форма
class MyVacancyIdView(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy.html', context={'form': VacancySendForm})

    def post(self, request):
        form = VacancySendForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('vacancy_send')
        return render(request, 'vacancies/vacancy.html', context={'form': form})


# список вакансии пользователя
class MyVacancyView(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': MyVacanciesForm,
        })