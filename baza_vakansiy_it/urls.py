"""baza_vakansiy_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from vacancies.views import main_view, vacancies_view, vacancies_by_specialty, company_view, vacancy_view, mycompany_view, mycompany_create_view, mycompany_letsstart_view, myvacancy_view, myvacancy_create_view, vacancy_send, myvacancy_id_view, my_company_letstart, my_company_create, my_company, my_company_vacancies, my_company_vacancies_create, my_company_vacancy_id
from accounts.views import MyLoginView, MySignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:specialty>/', vacancies_by_specialty, name='vacancies_by_specialty'),
    path('vacancies/<pk>/', vacancy_view, name='vacancy'),
    path('companies/<str:company>/', company_view, name='company'),

    # Отправка заявки
    path('vacancies/<vacancy_id>/send/', vacancy_send, name='vacancy_send'),
    # предложение создать
    path('mycompany/letsstart/', my_company_letstart, name='letsstart_mycompany'),
    # пустая форма
    path('mycompany/create/', my_company_create, name='create_mycompany'),
    # заполненная форма
    path('mycompany/', my_company, name='mycompany'),
    # пустая форма
    path('mycompany/vacancies/create/', my_company_vacancies_create, name='myvacancy_create'),
    # заполненная форма
    path('mycompany/vacancies/<vacancy_id>', my_company_vacancy_id, name='myvacancy_id'),

    #список
    path('mycompany/vacancies/', my_company_vacancies, name='myvacancy'),


    path('register/', MySignupView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
