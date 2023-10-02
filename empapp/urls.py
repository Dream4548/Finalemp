from django.urls import path
from empapp.views import index, about, ps, pvd, ass


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('purchase', ps, name='purchase'),
    path('Providing_customers', pvd, name='pvd' ),
    path('After_sale', ass, name='ass' ),
    
    
]