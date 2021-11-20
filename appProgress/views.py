from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def singin(request):
    return render(request, 'sing_in.html')