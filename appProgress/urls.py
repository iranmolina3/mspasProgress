from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('sesion', sing_in.as_view(), name='sing_in')
]