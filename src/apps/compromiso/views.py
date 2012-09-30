#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LATEST NEWS FROM ANDINA
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from lxml.html import parse
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from django.utils.encoding import smart_unicode, force_unicode

def andina():
    url = 'http://www.andina.com.pe/Espanol/aspa2012/index.aspx'
    root = parse(url).getroot()
    news = []
    noticias = root.xpath("//table[@id='dlstNoticia']")[0]
    for noticia in noticias:
        news.append(dict(
            titular = noticia.xpath("./td[1]//h5")[0].text_content().encode("utf-8"),
            texto = noticia.xpath("./td[1]//h6")[0].text_content().encode("utf-8"),
            ))
    return news

def andina_news(request):
    import json
    data = json.dumps(andina(), indent=2)
    return HttpResponse(data,mimetype='application/json')

def index(request):    
    return render_to_response('andina.html', {}, context_instance=RequestContext(request),)
