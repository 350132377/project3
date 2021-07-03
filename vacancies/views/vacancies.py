from django.shortcuts import render, redirect
from vacancies.models import Specialty, Vacancy, Company
from django.shortcuts import get_object_or_404
from django.views import View
from vacancies.forms import ApplicationSendForm, MyVacanciesForm

def vacancy_send(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/sent.html', context={
        'vacancy': vacancy,
    })

# список
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

def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
    })

class ApplicationSendView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'vacancies/vacancy.html', context={
            'form': ApplicationSendForm,
            'vacancy': vacancy,
        })
# не работает отправка отклика
    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationSendForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('vacancy_send', kwargs={'vacancy_id': pk})
        return render(request, 'vacancies/vacancy.html', context={
            'form': form,
            'vacancy': vacancy,
        })

# список вакансии пользователя
class MyVacancyView(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': MyVacanciesForm,
        })