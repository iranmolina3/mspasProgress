from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('singin', sing_in.as_view(), name='sing_in'),
    path('register', register.as_view(),  name='register'),
    path('dashboard', dasboard.as_view(), name='dashboard')
]