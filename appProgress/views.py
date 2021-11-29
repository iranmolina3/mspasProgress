from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

"""def home(request):
    return render(request, 'index.html')"""

"""
class padre = View
class hijo = TemplateView defined only GET
"""

"""class home(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')"""

class home(TemplateView):
    template_name = 'index.html'

"""class sing_in(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'sing_in.html')"""

class sing_in(TemplateView):
    template_name = 'sing_in.html'

