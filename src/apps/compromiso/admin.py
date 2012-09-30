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
    list_display = ('codigo','origen','ubigeo','estado',)
    list_display_links = ('origen','codigo',)
    list_filter = ('origen','estado','ubigeo',)
    search_fields = ['^origen', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : ('origen','ubigeo','estado',),
            }
        ),
    )
    form = FormOrigen

    class Media:
        js = ('js/jquery.js',)

class FormRemitente(forms.ModelForm):
    ubigeo = UbigeoFormField(ubigeo=constant.ONLY_PERU)

    class Meta:
        model = Remitente

class AdminRemitente(admin.ModelAdmin):
    list_display = ('codigo','remitente','direccion','fono','email','ubigeo','estado',)
    list_display_links = ('remitente','codigo',)
    list_filter = ('remitente','estado','ubigeo',)
    search_fields = ['^remitente', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('remitente','fono','email',),),
            }
        ),
        (None, {
                'fields' : ('ubigeo','direccion','estado',),
            }
        ),
    )
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

class AdminTipoCompromiso(admin.ModelAdmin):
    list_display = ('codigo','tipo','estado',)
    list_display_links = ('tipo','codigo',)
    list_filter = ('tipo','codigo','estado',)
    search_fields = ['^tipo', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('tipo','estado',),),
            }
        ),
    )

class AdminRazonSocial(admin.ModelAdmin):
    list_display = ('codigo','razon_social','estado',)
    list_display_links = ('razon_social','codigo',)
    list_filter = ('razon_social','codigo','estado',)
    search_fields = ['^razon_social', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('razon_social','estado',),),
            }
        ),
    )

class AdminSector(admin.ModelAdmin):
    list_display = ('codigo','sector','estado',)
    list_display_links = ('sector','codigo',)
    list_filter = ('sector','codigo','estado',)
    search_fields = ['^sector', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('sector','estado',),),
            }
        ),
    )

class AdminCategoria(admin.ModelAdmin):
    list_display = ('codigo','categoria','estado',)
    list_display_links = ('categoria','codigo',)
    list_filter = ('categoria','estado',)
    search_fields = ['^categoria', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('categoria','estado',),),
            }
        ),
    )

class AdminCargo(admin.ModelAdmin):
    list_display = ('codigo','cargo','estado',)
    list_display_links = ('cargo','codigo',)
    list_filter = ('cargo','estado',)
    search_fields = ['^cargo', ]
    radio_fields = {"estado" : admin.HORIZONTAL,}
    list_per_page= 25
    list_max_show_all=50
    actions_on_top = True
    actions_on_bottom = False
    fieldsets = (
        (None, {
                'fields' : (('cargo','estado',),),
            }
        ),
    )

admin.site.register(TipoCompromiso, AdminTipoCompromiso)
admin.site.register(RazonSocial, AdminRazonSocial)
admin.site.register(Sector, AdminSector)
admin.site.register(Origen, AdminOrigen)
admin.site.register(Categoria, AdminCategoria)
admin.site.register(Cargo, AdminCargo)
admin.site.register(Remitente, AdminRemitente)
admin.site.register(Compromiso, AdminCompromiso)

