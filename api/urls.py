from django.urls import path
from .views import *

urlpatterns = [   
    path('joyerias/', joyeria_lista),
    path('joyerias/<str:joyeria_id>', joyeria_detail),
    path('marcas/', marcas_lista),
]