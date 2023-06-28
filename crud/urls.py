from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('joyeria/', joyeria_lista, name="joyeria"),    
    path('joyeria/<str:joyeria_id>/delete', joyeria_delete, name="joyeria-delete"),
    path('joyeria/detail/<str:joyeria_id>', joyeria_detail, name="joyeria-detail"),
    path('joyeria/edit/<str:joyeria_id>', joyeria_update, name="joyeria-edit"),
    path('joyeria/new/', joyeria_new, name="joyeria-new"),
    path('joyeria/marca/<marca>', joyeria_by_marca, name="joyeria-marca"),
    path('joyeria/tipo/<tipo>',joyeria_by_tipo, name="joyeria-tipo"),
]