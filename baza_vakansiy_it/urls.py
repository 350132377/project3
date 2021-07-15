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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from vacancies.views.company import MyCompanyView, MyCompanyCreateView, MyCompanyStartView
from vacancies.views.company import custom_handler404_company, custom_handler500_company
from vacancies.views.main import custom_handler404_main, custom_handler500_main
from vacancies.views.main import main_view, company_view, vacancies_by_specialty
from vacancies.views.vacancies import custom_handler404_vacancies, custom_handler500_vacancies
from vacancies.views.vacancies import vacancies_view, vacancy_send, MyVacanciesListView, MyVacancyView, \
    ApplicationSendView, MyVacancyCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:specialty>/', vacancies_by_specialty, name='vacancies_by_specialty'),
    path('companies/<str:company>/', company_view, name='company'),
    path('vacancies/<pk>/', ApplicationSendView.as_view(), name='application_vacancy'),

    path('vacancies/<vacancy_id>/send/', vacancy_send, name='vacancy_send'),
    path('mycompany/vacancies/', MyVacanciesListView.as_view(), name='myvacancy'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyVacancyView.as_view(), name='myvacancy_id'),
    path('mycompany/vacancies/create/', MyVacancyCreateView.as_view(), name='vacancy_create_form'),

    path('mycompany/letsstart/', MyCompanyStartView.as_view(), name='letsstart_mycompany'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='company_create'),
    path('mycompany/', MyCompanyView.as_view(), name='mycompany'),

    path('accounts/', include('accounts.urls')),

    path('404/', custom_handler404_company),
    path('505/', custom_handler500_company),

    path('404/', custom_handler404_vacancies),
    path('505/', custom_handler500_vacancies),

    path('404/', custom_handler404_main),
    path('505/', custom_handler500_main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404_company = custom_handler404_company
handler500_company = custom_handler500_company

handler404_vacancies = custom_handler404_vacancies
handler500_vacancies = custom_handler500_vacancies

handler404_main = custom_handler404_main
handler500_main = custom_handler500_main
