from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def index(request):
    context = {}
   
       
    detail = models.detail.objects.all().order_by("id")
   
    context ['detail'] = detail
    
    return render(request,'index.html',context)

def about(request):
    return render (request,'about.html')

def ps(request):
    context = {}
   
       
    detail = models.detail.objects.filter(detail_department=1).order_by("id")
   
    context ['detail'] = detail
    
    return render(request,'ps.html',context)

def pvd(request):
    context = {}
   
       
    detail = models.detail.objects.filter(detail_department=2).order_by("id")
   
    context ['detail'] = detail
    
    return render(request,'pvd.html',context)

def ass(request):
    context = {}
   
       
    detail = models.detail.objects.filter(detail_department=3).order_by("id")
   
    context ['detail'] = detail
    
    return render(request,'ass.html',context)