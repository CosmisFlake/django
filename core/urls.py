from django.urls import path
from .views import *


urlpatterns = [
    path('', root),
    path('inicio/', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('catalogo/', catalogo, name='catalogo'),
    path('servicios/', servicios, name='servicios'),
    path('catalogo/marca/<marca>', catalogo_by_marca, name='catalogo-marca'),
]