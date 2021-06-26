from django.contrib import admin
from vacancies.models import Vacancy, Company, Application, Specialty, User


class VacancyAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass

class SpecialtyAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(User, UserAdmin)
