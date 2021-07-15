from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from vacancies.forms import MyCompanyForm, MyCompanyCreateForm
from vacancies.models import Company


class MyCompanyStartView(View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            return redirect('mycompany')
        return render(request, 'vacancies/company-start.html')


class MyCompanyCreateView(View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            return redirect('mycompany')
        return render(request, 'vacancies/company-create.html', context={'form': MyCompanyCreateForm})

    def post(self, request):
        form = MyCompanyCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            return redirect('mycompany')
        return render(request, 'vacancies/company-create.html', context={'form': form})

class MyCompanyView(View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            initial = {
                'title': company.title,
                'employee_count': company.employee_count,
                'location': company.location,
                'description': company.description,
            }
            form = MyCompanyForm(initial=initial)
            context = {
                'company': company,
                'form': form,
            }
            return render(request, 'vacancies/company-edit.html', context=context)
        else:
            return redirect('company_start')

    def post(self, request):
        form = MyCompanyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save()
            messages.success(request, 'Информация о компании обновлена')
            return redirect('mycompany')
        return render(request, 'vacancies/company-create.html', context={'form': form})

def custom_handler404_company(request, exception=None, template_name='vacancies/errors/404.html'):
    return render(request, template_name)

def custom_handler500_company(request, template_name='vacancies/errors/505.html'):
    return render(request, template_name)
