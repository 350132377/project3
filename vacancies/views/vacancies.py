from django.shortcuts import render, redirect
from vacancies.models import Specialty, Vacancy, Company
from django.shortcuts import get_object_or_404
from django.views import View
from vacancies.forms import ApplicationSendForm, MyVacanciesForm
from django.contrib import messages
from django.template import RequestContext


def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
    })

def vacancy_send(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/sent.html', context={
        'vacancy': vacancy,
    })

class ApplicationSendView(View):
    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        return render(request, 'vacancies/vacancy.html', context={
            'form': ApplicationSendForm,
            'vacancy': vacancy,
        })

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = ApplicationSendForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('vacancy_send', vacancy_id=pk)
        return render(request, 'vacancies/vacancy.html', context={
            'form': form,
            'vacancy': vacancy,
        })

class MyVacanciesListView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner_id=request.user.id)
        except Company.DoesNotExist:
            return redirect('letsstart_mycompany')
        vacancies = Vacancy.objects.filter(company_id=company.id)
        return render(request, 'vacancies/vacancy-list.html', context={
            'vacancies': vacancies,
        })


class MyVacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        if vacancy:
            initial = {
                'title': vacancy.title,
                'specialty': vacancy.specialty,
                'skills': vacancy.skills,
                'description': vacancy.description,
                'salary_min': vacancy.salary_min,
                'salary_max': vacancy.salary_max,
                'published_at': vacancy.published_at,
            }
            form = MyVacanciesForm(initial=initial)
            context = {
                'vacancy': vacancy,
                'form': form,
            }
            return render(request, 'vacancies/vacancy-edit.html', context=context)
        else:
            return redirect('vacancy_create_form')

    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        form = MyVacanciesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            messages.success(request, 'Вакансия обновлена')
            return redirect('myvacancy_id', vacancy_id=vacancy_id)
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': form,
            'vacancy': vacancy,
        })

class MyVacancyCreateView(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-create.html', context={
            'form': MyVacanciesForm,
        })

    def post(self, request, pk, code):
        form = MyVacanciesForm(request.POST)
        form.specialty_id = Specialty.objects.filter(code=code)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            messages.success('Вакансия обновлена')
            return redirect('myvacancy_id', vacancy_id=pk)
        return render(request, 'vacancies/vacancy-create.html', context={
            'form': form,
        })

def custom_handler404_vacancies(request, exception=None, template_name='vacancies/errors/404.html'):
    return render(request, template_name)

def custom_handler500_vacancies(request, template_name='vacancies/errors/505.html'):
    return render(request, template_name)
