from django.db import models
from datetime import datetime

# Create your models here.
from django.db.transaction import on_commit


class tbl_persona(models.Model):
    pk_persona = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    primer_nombre = models.CharField('primer nombre', max_length=25, null=False, blank=False)
    segundo_nombre = models.CharField('segundo nombre', max_length=25, null=True, blank=True)
    primer_apellido = models.CharField('primer apellido', max_length=25, null=False, blank=False)
    segundo_apellido = models.CharField('segundo apellido', max_length=25, null=True, blank=True)
    cui = models.CharField('cui', max_length=25, null=False, blank=False)
    fecha_nacimiento = models.DateField('fecha de nacimiento', null=False, blank=False)
    direccion = models.TextField('adomicilio', null=False, blank=False)
    telefono = models.CharField('telefono', max_length=8, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)


class tbl_usuario(models.Model):
    pk_usuario = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    usuario = models.CharField('usuario', max_length=25, null=False, blank=False)
    contrasenia = models.CharField('contraseña', max_length=255, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)
    fk_persona = models.OneToOneField(tbl_persona, null=False, blank=False, on_delete=models.CASCADE)

class tbl_producto(models.Model):
    pk_producto = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)

class tbl_detalle_ejecucion(models.Model):
    pk_detalle_ejecucion = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)

class tbl_ejecucion(models.Model):
    pk_detalle_ejecucion = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)
    fk_detalle_ejecucion = models.ForeignKey(tbl_detalle_ejecucion, null=False, blank=False, on_delete=models.CASCADE)

class tbl_tipo_requerimiento(models.Model):
    pk_tipo_requerimiento = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)

class tbl_producto(models.Model):
    pk_producto = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    fecha_inicio = models.DateField('fecha inicio', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_fin = models.DateField('fecha fin', auto_now_add=False, auto_now=True, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)

class tbl_requerimiento(models.Model):
    pk_requerimiento = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    nombre = models.CharField('nombre', max_length=100, null=False, blank=False)
    descripcion = models.TextField('descripcion', null=True, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)
    fk_ejecucion = models.ForeignKey(tbl_ejecucion ,null=False, blank=False, on_delete=models.CASCADE)
    fk_tipo_requerimiento = models.ForeignKey(tbl_tipo_requerimiento, null=False, blank=False, on_delete=models.CASCADE)
    fk_producto = models.ForeignKey(tbl_producto, null=False, blank=False, on_delete=models.CASCADE)

class tbl_asignatura(models.Model):
    pk_asignatura = models.AutoField('identificador', primary_key=True, null=False, blank=False)
    fecha_inicio = models.DateField('fecha inicio', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_fin = models.DateField('fecha fin', auto_now_add=False, auto_now=True, null=False, blank=False)
    fecha_creacion = models.DateField('fecha creacion', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_modificacion = models.DateField('fecha modificacion', auto_now_add=False, auto_now=True, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)
    estatus = models.IntegerField('estatus', default=0, null=False, blank=False)
    fk_usuario = models.ForeignKey(tbl_usuario, null=False, blank=False, on_delete=models.CASCADE)
    fk_requerimiento = models.ForeignKey(tbl_requerimiento, null=False, blank=False, on_delete=models.CASCADE)

class tbl_nota_asignatura(models.Model):
    descripcion = models.TextField('descripcion', null=True, blank=False)
    fecha_creacion = models.DateField('fecha creacion', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_modificacion = models.DateField('fecha modificacion', auto_now_add=False, auto_now=True, null=False, blank=False)
    fk_asignatura = models.ForeignKey(tbl_asignatura, null=False, blank=False, on_delete=models.CASCADE)

class tbl_sub_asignatura(models.Model):
    descripcion = models.TextField('descripcion', null=True, blank=False)
    fecha_inicio = models.DateField('fecha inicio', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_fin = models.DateField('fecha fin', auto_now_add=False, auto_now=True, null=False, blank=False)
    fecha_creacion = models.DateField('fecha creacion', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_modificacion = models.DateField('fecha modificacion', auto_now_add=False, auto_now=True, null=False, blank=False)
    estado = models.BooleanField('activo/inactivo', default=True, null=False, blank=False)
    fk_asignatura = models.ForeignKey(tbl_asignatura, null=False, blank=False, on_delete=models.CASCADE)

class tbl_nota_sub_asignatura(models.Model):
    descripcion = models.TextField('descripcion', null=True, blank=False)
    fecha_creacion = models.DateField('fecha creacion', auto_now_add=True, auto_now=False, null=False, blank=False)
    fecha_modificacion = models.DateField('fecha modificacion', auto_now_add=False, auto_now=True, null=False, blank=False)
    fk_asignatura = models.ForeignKey(tbl_sub_asignatura, null=False, blank=False, on_delete=models.CASCADE)