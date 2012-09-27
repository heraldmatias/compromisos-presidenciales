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

admin.site.register(TipoCompromiso)
admin.site.register(RazonSocial)
admin.site.register(Sector)
admin.site.register(Origen)
admin.site.register(Categoria)
admin.site.register(Cargo)
admin.site.register(Remitente)
admin.site.register(Compromiso)
admin.site.register(DetalleCompromiso)

