from django.contrib import admin
from api.models import Company,Employee

class companyadmin(admin.ModelAdmin):
    list_display=['name','location','type',]
    search_fields=['name',]

class employeeadmin(admin.ModelAdmin):
    list_display=['name',]
    list_filter=['company',]

# Register your models here.
admin.site.register(Company, companyadmin)
admin.site.register(Employee,employeeadmin)