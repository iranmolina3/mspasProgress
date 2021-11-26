from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sing_in(request):
    return render(request, 'sing_in.html')