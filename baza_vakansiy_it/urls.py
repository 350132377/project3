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

from vacancies.views import main_view, vacancies_view, vacancies_by_specialty, company_view, vacancy_view, mycompany_view, mycompany_create_view, mycompany_letsstart_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:specialty>/', vacancies_by_specialty, name='vacancies_by_specialty'),
    path('vacancies/<str:vacancy>/', vacancy_view, name='vacancy'),
    path('companies/<str:company>/', company_view, name='company'),
    path('vacancies/<vacancy_id>/send/'),
    path('mycompany/letsstart/', mycompany_letsstart_view.as_view(), name='letsstart_mycompany'),
    path('mycompany/create/', mycompany_create_view.as_view(), name='create_mycompany'),
    path('mycompany/', mycompany_view.as_view(), name='mycompany'),
    path('mycompany/vacancies/'),
    path('mycompany/vacancies/create/'),
    path('mycompany/vacancies/<vacancy_id>'),
    path('login/'),
    path('register/'),
    path('logout/'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
