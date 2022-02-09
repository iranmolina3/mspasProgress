from django.core.mail.backends import smtp
from django.forms import EmailInput
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.models import User

from decouple import config
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.

from .forms import *

# Validation exist email

from email_validate import validate, validate_or_fail


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
    # print('VARIABLE DE ENTORNO: ' + config('EMAIL_PASSWORD'))
    def post(self, request):
        password_user = request.POST['mypassword']
        name_user = request.POST['myuser']

        model_user = User.objects.get(username=name_user)

        print('USER: ', model_user.get_username(), 'PASS:', model_user.check_password(password_user))
        template_name = 'dashboard.html'
        return render(request, template_name)
    template_name = 'auth-signin.html'

"""
* se validara la creacion del usuario
* si y solo si el usuario cumple con
* los siguientes criterios:
    - @mspas.gob.gt
    - existencia del correo
"""

class register(CreateView):
    def get(self, request):
        template_name = 'auth-signup.html'
        return render(request, template_name, {'formUsuario':formUsuario, 'formPersona':formPersona})
    def post(self, request):
        usuario = request.POST['usuario']
        subtring_usuario = usuario[:usuario.find('@')]
        contrasenia = request.POST['contrasenia']
        # -- DATOS PERSONALES
        primer_nombre = request.POST['primer_nombre']
        primer_apellido = request.POST['primer_apellido']

        validate_myemail = validate(email_address=usuario, check_smtp=True)
        # print('RESULTADO', validate_myemail, ', correo: ', usuario)
        if validate_myemail:
            model_user = User.objects.create_user(subtring_usuario, usuario, contrasenia)
            model_user.save()
            send_mail(usuario)
            model_persona = tbl_persona(primer_nombre=primer_nombre, primer_apellido=primer_apellido, fk_usuario=model_user)
            model_persona.save()
            return redirect('appProgress:sing_in')
        else:
            return redirect('appProgress:register')
    success_url = reverse_lazy('appProgress:sing_in')

class dasboard(TemplateView):
    template_name = 'dashboard.html'


def send_mail(mail):
    context = {'mail': mail}
    template = get_template('email/email_register.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'Developer iran_mx2',
        settings.EMAIL_HOST_USER,
        [mail],
        cc=[]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

