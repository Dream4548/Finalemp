from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.gender)
class genderAdmin(admin.ModelAdmin):
    list_display = [
        'gender'
    ]
    
@admin.register(models.Educationlevel)
class EducationlevelAdmin(admin.ModelAdmin):
    list_display = [
        'Educationlevel'
    ]
   
@admin.register(models.department)
class departmentAdmin(admin.ModelAdmin):
    list_display = [
        'department'
    ] 
@admin.register(models.detail)
class detailAdmin(admin.ModelAdmin):
    list_display = [
        'detail_name',
        'detail_gender',
        'detail_age',
        #'class_Educationlevel',
        'detail_department',
    ]