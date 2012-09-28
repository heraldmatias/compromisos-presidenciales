# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from compromiso.models import TipoCompromiso
from compromiso.models import RazonSocial
from compromiso.models import Sector
from compromiso.models import Origen
from compromiso.models import Categoria
from compromiso.models import Cargo
from compromiso.models import Remitente
from compromiso.models import Compromiso
from compromiso.models import DetalleCompromiso
from ubigeo.fields import UbigeoFormField
from ubigeo import constant

class FormOrigen(forms.ModelForm):
    ubigeo = UbigeoFormField(ubigeo=constant.ONLY_PERU)

    class Meta:
        model = Origen

class AdminOrigen(admin.ModelAdmin):
    form = FormOrigen

    class Media:
        js = ('js/jquery.js',)

class FormRemitente(forms.ModelForm):
    ubigeo = UbigeoFormField(ubigeo=constant.ONLY_PERU)

    class Meta:
        model = Remitente

class AdminRemitente(admin.ModelAdmin):
    form = FormRemitente

    class Media:
        js = ('js/jquery.js',)

class AdminDetalle(admin.StackedInline):
    model = DetalleCompromiso
    extra = 0

class AdminCompromiso(admin.ModelAdmin):
    list_display = ('codigo','expediente','sip','remitente','tipo','origen','sector','categoria','estado',)
    list_display_links = ('expediente','codigo',)
    list_filter = ('tipo','origen','categoria','estado')
    search_fields = ['^expediente','^tipo']
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    inlines = [
        AdminDetalle,
    ]
    fieldsets = (
        (None, {
                'fields' : (('tipo','categoria','estado'),),
            }
        ),
        (None, {
                'fields' : ('origen','razon_social',('remitente','sector'),),
            }
        ),
        (None, {
                'fields' : (('expediente','sip',),'descripcion',),
            }
        ),
    )

    class Media:
        css = {
            "all": ('css/compromiso.css',)
        }

admin.site.register(TipoCompromiso)
admin.site.register(RazonSocial)
admin.site.register(Sector)
admin.site.register(Origen, AdminOrigen)
admin.site.register(Categoria)
admin.site.register(Cargo)
admin.site.register(Remitente, AdminRemitente)
admin.site.register(Compromiso, AdminCompromiso)

