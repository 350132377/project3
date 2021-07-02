from django.shortcuts import render, redirect
from django.views import View
from vacancies.forms import MyCompanyForm, MyCompanyCreateForm
from vacancies.models import Company


# work предложение создать
def my_company_letstart(request):
    return render(request, 'vacancies/company-create.html')
# work пустая форма
def my_company_create(request):
    return render(request, 'vacancies/company-create.html')
# форма заполненная форма
def my_company(request):
    return render(request, 'vacancies/company-edit.html', context={
        'company': Company,
    })

#заполненная форма не работает компания пользователя
class MyCompanyView(View):
    def get(self, request):
        form = MyCompanyForm()
        return render(request, 'vacancies/company-edit.html', context={'form': form})

    def post(self, request):
        form = MyCompanyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.update()
            return redirect('mycompany')
        else:
            form = MyCompanyForm()
        return render(request, 'vacancies/company-create.html', context={'form': form})

# пустая форма компания пользователя
class MyCompanyCreateView(View):
    def get(self, request):
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('mycompany')
        return render(request, 'vacancies/company-edit.html', context={'form': form})
