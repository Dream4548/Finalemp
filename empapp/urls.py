from django.urls import path
from empapp.views import index


urlpatterns = [
    path('', index, name='index')
]