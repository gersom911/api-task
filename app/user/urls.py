
from django.urls import path
from .views import registro, index 

urlpatterns = [
    #rutas de interiores
    
    # rutas exteriores
   
    path('',  registro, name = 'registro'),
    
    
    
    
]