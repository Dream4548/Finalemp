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
    detail_name = models.CharField(max_length=100)
    detail_lastname = models.CharField(max_length=100, default="ไม่ระบุ")
    detail_gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    detail_age = models.IntegerField()
    detail_education = models.ForeignKey(education, on_delete=models.CASCADE)
    detail_department = models.ForeignKey(department, on_delete=models.CASCADE)


    def __str__(self):
        return self.detail_name