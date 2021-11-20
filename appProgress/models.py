from django.db import models

# Create your models here.

class tbl_persona(models.Model):
    pk_persona = models.AutoField(primary_key=True, null=False, blank=False)
    primer_nombre = models.CharField('primer nombre', max_length=25, null=False, blank=False)
    segundo_nombre = models.CharField('segundo nombre', max_length=25, null=True, blank=True)
    primer_apellido = models.CharField('primer apellido', max_length=25, null=False, blank=False)
    segundo_apellido = models.CharField('segundo apellido', max_length=25, null=True, blank=True)
    cui = models.CharField('cui', max_length=25, null=False, blank=False)
    fecha_nacimiento = models.DateField('fecha de nacimiento', null=False, blank=False)
    direccion = models.TextField('adomicilio', null=False, blank=False)
    telefono = models.CharField('telefono', max_length=8, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', null=False, blank=False)