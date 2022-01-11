from django import forms
from .models import *

class formPersona(forms.ModelForm):
    class Meta:
        model = tbl_persona
        fields = ['pk_persona', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'cui',
                  'fecha_nacimiento', 'direccion', 'telefono', 'estado']
        widgets = {
            'primer_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribre tu nombre',
                    'id': 'primer_nombre',
                    'name': 'primer_nombre'
                }
            ),
            'primer_apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribre tu apellido',
                    'id': 'primer_apellido',
                    'name': 'primer_apellido'
                }
            )
        }


class formUsuario(forms.ModelForm):
    class Meta:
        model = tbl_usuario
        fields = ['pk_usuario', 'usuario', 'contrasenia', 'estado', 'fk_persona']
        widgets = {
            'usuario': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Escribre tu correo MSPAS',
                    'id': 'usuario',
                    'name': 'usuario'
                }
            ),
            'contrasenia': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribre tu contraseña MSPAS',
                    'id': 'contrasenia',
                    'name': 'contrasenia'
                }
            )
        }
