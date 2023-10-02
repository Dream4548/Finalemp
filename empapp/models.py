from django.db import models

# Create your models here.

# หมวดหมู่รายวิชา
class gender(models.Model):
    gender = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.gender

class education(models.Model):
    education = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.education

class department(models.Model):
    department = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.department

# รายวิชา
class detail(models.Model):
    detail_name = models.CharField(max_length=100) #ชื่อ
    detail_lastname = models.CharField(max_length=100, default="") #นามสกุล
    detail_gender = models.ForeignKey(gender, on_delete=models.CASCADE) #เพศ
    detail_age = models.IntegerField() #อายุ
    detail_education = models.ForeignKey(education, on_delete=models.CASCADE) #ระดับการศึกษา
    detail_department = models.ForeignKey(department, on_delete=models.CASCADE) #แผนก


    def __str__(self):
        return self.detail_name