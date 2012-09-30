# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('compromiso.views',
    url(r'^noticias/json/$','andina_news', name='andina-news'),
    url(r'^$','index', name='andina'),
)
