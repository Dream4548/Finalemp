from django.db import models

# Create your models here.

# หมวดหมู่รายวิชา
class gender(models.Model):
    gender = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.gender

class Educationlevel(models.Model):
    Educationlevel = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.Educationlevel

class department(models.Model):
    department = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.department

# รายวิชา
class detail(models.Model):
    detail_name = models.CharField(max_length=100)
    detail_gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    detail_age = models.IntegerField() # หน่วยกิต
    #detail_Educationlevel = models.ForeignKey(Educationlevel, on_delete=models.CASCADE) # หมวดหมู่รายวิชา
    detail_department = models.ForeignKey(department, on_delete=models.CASCADE) # หมวดหมู่รายวิชา


    def __str__(self):
        return self.detail_name