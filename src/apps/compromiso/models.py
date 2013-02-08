# -*- coding: utf-8 -*-
from django.db import models
from ubigeo.models import Ubigeo

ESTADO = (
    ('Pendiente','Pendiente',),
    ('Atendido Pendiente', 'Atendido Pendiente',),
    ('Atendido Cerrado','Atendido Cerrado',),
    ('Archivado','Archivado',),
)

FORMAS = (
    ('Institucional', 'Institucional',),
    ('Personal', 'Personal',),
    ('Visita', 'Visita',),
)

class Motivo(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80)

    def __unicode__(self):
        return u'%s' % self.nombre

class Viaje(models.Model):
    codigo = models.AutoField(primary_key=True)
    motivo = models.TextField(verbose_name=u'Motivo',
        null=True)
    fecha = models.DateField(verbose_name=u'Fecha',)
    ubigeo = models.ForeignKey(Ubigeo,verbose_name=u'Ubigeo')

    def __unicode__(self):
        return u'%s' % self.motivo

class TipoPedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre

class DetallePedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(TipoPedido)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre
    
class Autoridad(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Autoridad'
        verbose_name_plural = u'Autoridades'

class Derivado(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre

class Asignado(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre

class Institucion(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=80,)

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = u'Institución'
        verbose_name_plural = u'Instituciones'
#OLD MODELS    
#class TipoCompromiso(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
#    tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)
#
#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_tipo'
#        verbose_name = 'Tipo de compromiso'
#        verbose_name_plural = 'Tipos de compromisos'
#        ordering = ('tipo',)

#    def __unicode__(self):
#        return u'%s' % self.tipo

#RAZON SOCIAL
#class RazonSocial(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
#    razon_social = models.CharField(verbose_name = 'Razon Social', max_length = 100, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_razon_social'
#        verbose_name = 'Razon Social'
#        verbose_name_plural = 'Razon Social varias'
#        ordering = ('razon_social',)

#    def __unicode__(self):
#        return u'%s' % self.razon_social

#class Sector(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key=True)
#    sector = models.CharField(verbose_name = 'Sector Social', max_length = 100, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_sector'
#        verbose_name = 'Sector'
#        verbose_name_plural = 'Sectores'
#        ordering = ('sector',)

#    def __unicode__(self):
#        return u'%s' % self.sector

#class Origen(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
#    origen = models.CharField(verbose_name = 'Origen', max_length = 100, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)
#    ubigeo = models.ForeignKey(Ubigeo)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_origen'  
#        verbose_name = 'Origen'
#        verbose_name_plural = 'Origenes'
#        ordering = ('origen',)

#    def __unicode__(self):
#        return u'%s' % self.origen

#class Categoria(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
#    categoria = models.CharField(verbose_name = 'Categoría', max_length = 50, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_categoria'
#        verbose_name = 'Categoria'
#        verbose_name_plural = 'Categorias'
#        ordering = ('categoria', )

#    def __unicode__(self):
#        return u'%s' % self.categoria

#class Cargo(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
#    cargo = models.CharField(verbose_name = 'Cargo', max_length = 50, db_index = True)
#    estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_cargo'
#        verbose_name = 'Cargo'
#        verbose_name_plural = 'Cargos'
#        ordering = ('cargo', )

#    def __unicode__(self):
#        return u'%s' % self.cargo

#class Remitente(models.Model):
#    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
#    remitente = models.CharField(verbose_name = 'Remitente', max_length = 150, db_index = True)
#    direccion = models.TextField(verbose_name = 'Dirección', null= True, blank = True)
#    fono = models.CharField(verbose_name='Telefono', max_length=25,)
#    email = models.EmailField(verbose_name='Email', max_length=135, unique=True)
#    ubigeo = models.ForeignKey(Ubigeo)
#    estado = models.IntegerField(verbose_name = 'Estado' , choices = ESTADO, default = 0)

#    class Meta:
#        db_tablespace = 'pg_default'
#        db_table = 'compromiso_remitente'
#        verbose_name = 'Remitente'
#        verbose_name_plural = 'Remitentes'
#        ordering = ('remitente', )

#    def __unicode__(self):
#        return u'%s' % self.remitente
class Seguimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name=u'Fecha')
    descripcion = models.TextField(verbose_name=u'Descripción')

    def __unicode__(self):
        return u'%20s' % self.descripcion

class Compromiso(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    #tipo = models.ForeignKey(TipoCompromiso, verbose_name='Tipo de pedido', db_index = True)
    #categoria = models.ForeignKey(Categoria, verbose_name='Categoría', db_index = True)
    institucion = models.ForeignKey(Institucion,
        verbose_name=u'Institución', null=True, blank=True)
    motivo = models.ForeignKey(Motivo,
        verbose_name=u'Motivo')
    viaje = models.ForeignKey(Viaje,
        verbose_name=u'Viaje', null=True,blank=True)
    formapedido = models.CharField(verbose_name=u'Forma Pedido',
        choices=FORMAS, max_length=20)
    persona = models.CharField(verbose_name=u'Persona',
        max_length=200)
    dni = models.CharField(verbose_name=u'DNI',
        max_length=8, null=True,blank=True)
    direccion = models.CharField(verbose_name=u'Dirección',
        max_length=250, null=True, blank=True)
    telefono = models.CharField(verbose_name=u'Teléfono',
        max_length=10, null=True, blank=True)
    autoridad = models.ForeignKey(Autoridad)
    #estado = models.IntegerField(verbose_name = 'Estado', choices = ESTADO, default = 0)
    #origen = models.ForeignKey(Origen, verbose_name='Origen Pedido', db_index = True)
    #razon_social = models.ForeignKey(RazonSocial, verbose_name='Razon Social')
    #remitente = models.ForeignKey(Remitente, verbose_name= 'Remitente')
    #sector = models.ForeignKey(Sector, verbose_name= 'Sector')
    #expediente = models.CharField(verbose_name= 'Expediente', max_length = 10, db_index = True)
    #sip = models.CharField(verbose_name= 'SIP', max_length = 10, db_index = True)
    #descripcion = models.TextField(verbose_name = 'Descripcion',)

    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_compromiso'
        verbose_name = 'Compromiso Presidencial'
        verbose_name_plural = 'Compromisos Presidenciales'
        ordering = ('codigo', )

    def __unicode__(self):
        return u'%s' % self.persona

class DetalleCompromiso(models.Model):
    codigo = models.AutoField(verbose_name = 'Código', primary_key = True)
    nombre = models.CharField(verbose_name=u'Nombre',
        max_length=100)
    estado = models.CharField(choices=ESTADO,max_length=20)
    tipopedido = models.ForeignKey(TipoPedido)
    detalle = models.ForeignKey(DetallePedido)
    numero = models.CharField(verbose_name=u'Número',
        max_length=10, 
        null = True, blank=True)
    expediente = models.CharField(verbose_name=u'Expediente',
        max_length=10,
        null = True, blank=True)
    descripcion = models.TextField(verbose_name = 'Descripción',
        null=True)
    derivado = models.ForeignKey(Derivado)
    fecha_derivado = models.DateField(verbose_name=u'Derivado Tramite',)
    asignado = models.ForeignKey(Asignado)
    fecha_asignado = models.DateField(verbose_name=u'Ingreso Tramite',)
    compromiso = models.ForeignKey(Compromiso, verbose_name='Compromiso')
    seguimientos = models.ManyToManyField(Seguimiento)
    class Meta:
        db_tablespace = 'pg_default'
        db_table = 'compromiso_compromiso_detalle'
        verbose_name = 'Detalle Compromiso'
        verbose_name_plural = 'Detalles Compromiso'
        ordering = ('fecha_asignado', )

    def __unicode__(self):
        return u'%20s' % self.nombre

