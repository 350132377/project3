from django.shortcuts import render, redirect
from django.views import View
from vacancies.models import Company, Specialty, Vacancy
from vacancies.forms import MyCompanyCreateForm, MyCompanyForm, MyVacanciesCreateForm, MyVacanciesForm, VacancySendForm
from django.shortcuts import get_object_or_404
# work
def main_view(request):
    return render(request, 'vacancies/index.html', context={
        'specialties': Specialty.objects.all(),
        'companies': Company.objects.all(),
    })
# work
def vacancies_view(request):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.all(),
    })
# work
def vacancy_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'vacancies/vacancy.html', context={
        'vacancy': vacancy,
        'company': company,
    })
# work
def vacancies_by_specialty(request, specialty):
    return render(request, 'vacancies/vacancies.html', context={
        'specialities': Specialty.objects.filter(code=specialty),
    })
# work
def company_view(request, company):
    return render(request, 'vacancies/company.html', context={
        'companies': Company.objects.filter(title=company),
    })

class mycompany_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-edit.html', context={'form': MyCompanyForm})

    def post(self, request):
        form = MyCompanyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.update()
            return redirect('mycompany')
        return render(request, 'vacancies/company-edit.html', context={'form': form})
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
class myvacancy_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-list.html', context={
            'form': MyVacanciesForm,
        })

#work
class mycompany_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('mycompany')
        return render(request, 'vacancies/company-edit.html', context={'form': form})
#!!!!!!!!!!!!!!
class myvacancy_create_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={'form': MyVacanciesCreateForm})

    def post(self, request):
        form = MyVacanciesCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy-list.html', context={'form': form})

class mycompany_letsstart_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('mycompany')
        return render(request, 'vacancies/company-create.html', context={'form': form})
# форма не появляется
class vacancy_send(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy.html', context={'form': VacancySendForm})

    def post(self, request):
        form = VacancySendForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy.html', context={'form': form})

class myvacancy_id_view(View):
    def get(self, request):
        return render(request, 'vacancies/vacancy-edit.html', context={'form': VacancySendForm})

    def post(self, request):
        form = VacancySendForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.update()
            return redirect('myvacancy')
        return render(request, 'vacancies/vacancy-edit.html', context={'form': form})
