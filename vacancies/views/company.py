from django.shortcuts import render, redirect
from django.views import View
from vacancies.forms import MyCompanyForm, MyCompanyCreateForm
from vacancies.models import Company



class MyCompanyView(View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            return render(request, 'vacancies/company-edit.html', context={'form': MyCompanyForm})
        else:
            return redirect('letsstart_mycompany')

class MyCompanyStartView(View):
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
        return render(request, 'vacancies/company-edit.html', context={'form': form})


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
        return render(request, 'vacancies/company-edit.html', context={'form': form})
