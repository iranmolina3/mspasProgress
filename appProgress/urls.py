from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sesion', sing_in, name='sing_in')
]