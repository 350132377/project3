from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from baza_vakansiy_it.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=45)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=70)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=80)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def clean(self):
        if self.salary_min > self.salary_max:
            raise ValidationError('Минимальный порог зарплаты больше, чем максимальный!')


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="applications")
