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