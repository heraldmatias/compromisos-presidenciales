# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('compromiso.views',
    url(r'^noticias/json/$','andina_news', name='andina-news'),
    url(r'^presidencia/noticias/json/$','presidencia_noticias_news', name='presidencia-noticias'),
    #url(r'^$','index', name='andina'),
    #url(r'^prueba/$','tablep', name='tablep'),
)
