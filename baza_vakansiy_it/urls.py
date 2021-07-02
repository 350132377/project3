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
from vacancies.views.main import main_view, company_view, vacancies_view, vacancies_by_specialty, vacancy_view
from vacancies.views.company import my_company_letstart, my_company_create, my_company, MyCompanyView, MyCompanyCreateView
from vacancies.views.vacancies import vacancy_send, my_company_vacancies, my_company_vacancies_create, my_company_vacancy_id, MyVacancyIdView, MyVacancyView
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:specialty>/', vacancies_by_specialty, name='vacancies_by_specialty'),
    path('vacancies/<pk>/', vacancy_view, name='vacancy'),
    path('companies/<str:company>/', company_view, name='company'),

    # вьюхи
    # Отправка заявки, отклик отправлен
    path('vacancies/<vacancy_id>/send/', vacancy_send, name='vacancy_send'),
    # предложение создать компанию
    path('mycompany/letsstart/', my_company_letstart, name='letsstart_mycompany'),
    # пустая форма компания
    path('mycompany/create/', my_company_create, name='create_mycompany'),
    # заполненная форма компания
    path('mycompany/', my_company, name='mycompany'),
    # список вакансий
    path('mycompany/vacancies/', my_company_vacancies, name='myvacancy'),
    # пустая форма вакансия
    path('mycompany/vacancies/create/', my_company_vacancies_create, name='myvacancy_create'),
    # заполненная форма вакансия
    path('mycompany/vacancies/<vacancy_id>', my_company_vacancy_id, name='myvacancy_id'),

    # формы
    # Доработайте страницу вакансии и отправку заявки «отклик отправлен»
    # Доработайте странички добавления и редактирования вакансии
    path('vacancies/<pk>/', MyVacancyIdView.as_view(), name='vacancy_form'),
    # Доработайте страничку информации о компании
    path('mycompany/', MyCompanyView.as_view(), name='company_form'),
    path('mycompany/', MyCompanyCreateView.as_view(), name='company_create_form'),
    # Доработайте страничку с вакансиями
    path('mycompany/vacancies/create/', MyVacancyView.as_view(), name='vacancy_create_form'),

    # авторизация, регистрация
    path('accounts/', include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
