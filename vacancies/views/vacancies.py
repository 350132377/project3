from django.shortcuts import render, redirect
from vacancies.models import Specialty, Vacancy, Company
from django.shortcuts import get_object_or_404
from django.views import View
from vacancies.forms import ApplicationSendForm, MyVacanciesForm



# work
def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
    })
# work
def vacancy_send(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/sent.html', context={
        'vacancy': vacancy,
    })
# отклик на вакансию
# work
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

# список вакансии пользователя
# work
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

# просмотр вакансии
# work
class MyVacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': MyVacanciesForm,
            'vacancy': vacancy,
        })

    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        form = MyVacanciesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('myvacancy_id', vacancy_id=vacancy_id)
        return render(request, 'vacancies/vacancy-edit.html', context={
            'form': form,
            'vacancy': vacancy,
        })

# редактирование вакансии
class MyVacancyCreateView(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-create.html', context={
            'form': MyVacanciesForm,
        })

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, pk=pk)
        form = MyVacanciesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('myvacancy_id', vacancy_id=pk)
        return render(request, 'vacancies/vacancy-create.html', context={
            'form': form,
            'vacancy': vacancy,
        })
