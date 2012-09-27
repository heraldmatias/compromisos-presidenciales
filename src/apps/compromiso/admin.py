# -*- coding: utf-8 -*-
from django.contrib import admin
from compromiso.models import TipoCompromiso
from compromiso.models import RazonSocial
from compromiso.models import Sector
from compromiso.models import Origen
from compromiso.models import Categoria
from compromiso.models import Cargo
from compromiso.models import Remitente
from compromiso.models import Compromiso
from compromiso.models import DetalleCompromiso

class AdminGenerico(admin.ModelAdmin):
    pass

admin.site.register(TipoCompromiso, TipoCompromiso)
admin.site.register(TipoCompromiso, RazonSocial)
admin.site.register(TipoCompromiso, Sector)
admin.site.register(TipoCompromiso, Origen)
admin.site.register(TipoCompromiso, Categoria)
admin.site.register(TipoCompromiso, Cargo)
admin.site.register(TipoCompromiso, Remitente)
admin.site.register(TipoCompromiso, Compromiso)
admin.site.register(TipoCompromiso, DetalleCompromiso)

