# -*- coding: utf-8 -*-
from django.db import models
from ubigeo.models import Ubigeo

ESTADO = (
    (0, 'PENDIENTE',),
    (1, 'ATENDIDO PENDIENTE',),
    (2, 'ATENDIDO CERRADO',),
)

class TipoCompromiso(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
    tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_tipo'
        verbose_name = 'Tipo de compromiso'
        verbose_name_plural = 'Tipos de compromisos'
        ordering = ('tipo',)

    def __unicode__(self):
        return u'%s' % self.tipo

#RAZON SOCIAL
class RazonSocial(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
    razon_social = models.CharField(verbose_name = 'Razon Social', max_length = 100, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_razon_social'
        verbose_name = 'Razon Social'
        verbose_name_plural = 'Razon Social varias'
        ordering = ('razon_social',)

    def __unicode__(self):
        return u'%s' % self.razon_social

class Sector(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
    sector = models.CharField(verbose_name = 'Sector Social', max_length = 100, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_sector'
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ('sector',)

    def __unicode__(self):
        return u'%s' % self.sector

class Origen(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    origen = models.CharField(verbose_name = 'Origen', max_length = 100, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)
    ubigeo = models.ForeignKey(Ubigeo)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_origen'  
        verbose_name = 'Origen'
        verbose_name_plural = 'Origenes'
        ordering = ('origen',)

    def __unicode__(self):
        return u'%s' % self.origen

class Categoria(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    categoria = models.CharField(verbose_name = 'Categoría', max_length = 50, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('categoria', )

    def __unicode__(self):
        return u'%s' % self.categoria

class Cargo(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    cargo = models.CharField(verbose_name = 'Cargo', max_length = 50, db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ('cargo', )

    def __unicode__(self):
        return u'%s' % self.cargo

class Remitente(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    remitente = models.CharField(verbose_name = 'Remitente', max_length = 150, db_index = True)
    direccion = models.TextField(verbose_name = 'Dirección', null= True, blank = True)
    fono = models.CharField(verbose_name='Telefono', max_length=25,)
    email = models.EmailField(verbose_name='Email', max_length=135, unique=True)
    ubigeo = models.ForeignKey(Ubigeo)
    estado = models.IntegerField(verbose_name = 'Estado' , choices = ESTADO, default = 0)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_remitente'
        verbose_name = 'Remitente'
        verbose_name_plural = 'Remitentes'
        ordering = ('remitente', )

    def __unicode__(self):
        return u'%s' % self.remitente

class Compromiso(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    tipo = models.ForeignKey(TipoCompromiso, verbose_name='Tipo de pedido', db_index = True)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoría', db_index = True)
    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)
    origen = models.ForeignKey(Origen, verbose_name='Origen Pedido', db_index = True)
    razon_social = models.ForeignKey(RazonSocial, verbose_name='Razon Social')
    remitente = models.ForeignKey(Remitente, verbose_name= 'Remitente')
    sector = models.ForeignKey(Sector, verbose_name= 'Sector')
    expediente = models.CharField(verbose_name= 'Expediente', max_length = 10, db_index = True)
    sip = models.CharField(verbose_name= 'SIP', max_length = 10, db_index = True)
    descripcion = models.TextField(verbose_name = 'Descripcion',)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_compromiso'
        verbose_name = 'Compromiso Presidencial'
        verbose_name_plural = 'Compromisos Presidenciales'
        ordering = ('expediente', )

    def __unicode__(self):
        return u'%s' % self.expediente

class DetalleCompromiso(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    fecha = models.DateField(verbose_name = 'Fecha', max_length = 50, db_index = True)
    observacion = models.TextField(verbose_name = 'Obervación',)
    compromiso = models.ForeignKey(Compromiso, verbose_name='Compromiso')

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_compromiso_detalle'
        verbose_name = 'Detalle Compromiso'
        verbose_name_plural = 'Detalles Compromiso'
        ordering = ('fecha', )

    def __unicode__(self):
        return u'%20s' % self.observacion


"""
App for Alumno
"""
SEXO = (
        ('F','Femenino'),
        ('M','Masculino'),
        )

class Alumno(models.Model):
    codigo           = models.CharField('Código', max_length=10, blank=True, null=True)
    numero_matricula = models.CharField('Número Matricula', max_length=12, blank=True, null=True)
    apellido         = models.CharField('Apellido', max_length=200)
    nombre           = models.CharField('Nombre', max_length=200)
    dni              = models.CharField('D.N.I.', max_length=12, unique=True)
    telefono         = models.CharField('Teléfono', max_length=10, blank=True, null=True)
    sexo             = models.CharField('Sexo', max_length=1, choices = SEXO, blank=True, null=True)
    celular          = models.CharField('Celular', max_length=12, blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', )
    direccion        = models.TextField('Dirección', blank=True, null=True)
    foto             = models.ImageField('Foto', upload_to='alumno/', blank=True, null=True)
    apoderado        = models.CharField('Apoderado', max_length=250)
    email            = models.EmailField('E-Mail')
    matriculado      = models.BooleanField('Matriculado', default=False)

    class Meta:
        db_table = 'alumno_alumno'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        unique_together = ('dni','apellido', 'nombre','codigo',)
        ordering = ["id"]

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return u'%s,  %s' % (self.apellido, self.nombre)
