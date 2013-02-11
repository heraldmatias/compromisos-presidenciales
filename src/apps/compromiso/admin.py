# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from compromiso.models import Seguimiento
from compromiso.models import Motivo
from compromiso.models import Viaje
from compromiso.models import TipoPedido
from compromiso.models import DetallePedido
from compromiso.models import Autoridad
from compromiso.models import Derivado
from compromiso.models import Asignado
from compromiso.models import Compromiso
from compromiso.models import Institucion
from compromiso.models import DetalleCompromiso
from ubigeo.fields import UbigeoFormField
from ubigeo import constant

class FormOrigen(forms.ModelForm):
    ubigeo = UbigeoFormField(ubigeo=constant.ONLY_PERU)

    class Meta:
        model = Viaje

class AdminViaje(admin.ModelAdmin):
    list_display = ('codigo','motivo','fecha','ubigeo',)
    list_display_links = ('codigo','motivo',)
    list_filter = ('motivo','ubigeo',)
    search_fields = ['^motivo', ]    
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : ('motivo','fecha','ubigeo',),
            }
        ),
    )
    form = FormOrigen

class AdminSeguimientoI(admin.StackedInline):
    model = Seguimiento
    extra = 0

class AdminDetalle(admin.StackedInline):
    model = DetalleCompromiso
    extra = 0
    fieldsets = (
        (None, {
                'fields' : (('nombre','estado',),
                    ('tipopedido','detalle',),
                    ('descripcion',),
                    ('numero','expediente',),
                    ('fecha_derivado','fecha_asignado',),
                    ('derivado','asignado',),
                    ('seguimientos',),),
            }
        ),              
    )
    def queryset(self, request):
        qs = super(AdminDetalle, self).queryset(request)
        print qs
        return qs
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        print db_field
        #if db_field.name == "cars":
        #    kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super(AdminDetalle, self).formfield_for_manytomany(db_field, request, **kwargs)

class AdminCompromiso(admin.ModelAdmin):
    list_display = ('codigo','motivo','formapedido','persona','dni','direccion','telefono','autoridad',)
    list_display_links = ('motivo','codigo',)
    list_filter = ('motivo','codigo')
    search_fields = ['^persona',]
    radio_fields = {"formapedido" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    inlines = [
        AdminDetalle,
    ]
    fieldsets = (
        (None, {
                'fields' : (('motivo','viaje'),('formapedido','institucion',),),
            }
        ),
        (None, {
                'fields' : (('persona','autoridad'),('dni','telefono'),('direccion',),),
            }
        ),        
    )

    class Media:
        css = {
            "all": ('css/compromiso.css',)
        }        
        js = ('js/options.js',)

class AdminMotivo(admin.ModelAdmin):
    list_display = ('codigo','nombre',)
    list_display_links = ('codigo',)
    list_filter = ('nombre',)
    search_fields = ['^nombre', ]    
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('nombre',),),
            }
        ),
    )

class AdminDetallePedido(admin.ModelAdmin):
    list_display = ('codigo','nombre','pedido',)
    list_display_links = ('codigo',)
    list_filter = ('nombre','pedido')
    search_fields = ['^nombre', ] 
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('pedido','nombre',),),
            }
        ),
    )

class AdminSeguimiento(admin.ModelAdmin):
    list_display = ('codigo','fecha','descripcion',)
    list_display_links = ('codigo',)
    list_filter = ('fecha',)
    search_fields = ['^descripcion', ]    
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('fecha',),('descripcion',),),
            }
        ),
    )
admin.site.register(Viaje, AdminViaje)
admin.site.register(TipoPedido, AdminMotivo)
admin.site.register(Autoridad, AdminMotivo)
admin.site.register(Derivado, AdminMotivo)
admin.site.register(Asignado, AdminMotivo)
admin.site.register(Institucion, AdminMotivo)
admin.site.register(Seguimiento, AdminSeguimiento)
admin.site.register(DetallePedido, AdminDetallePedido)
admin.site.register(Compromiso, AdminCompromiso)