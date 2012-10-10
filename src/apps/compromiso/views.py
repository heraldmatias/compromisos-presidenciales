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
    return news
    titu = u""
    text = u""
    noticias = root.xpath("//table[@id='dlstNoticia']")[0]
    noticia = None
    for c in range(1,4):
        noticia = noticias[c]
        titu = u'%s' % noticia.xpath("./td[1]//h5")[0].text_content()
        link = u'%s' % noticia.xpath("./td[1]//a/@href")[0].replace("../","http://www.andina.com.pe/Espanol/")
        texta = u'%s' % noticia.xpath("./td[1]//h6")[0].text_content()
        hora = u'%s' % noticia.xpath("./td[1]//h4")[0].text_content()
        news.append(dict(
            titular = titu.encode('latin-1'),
            texto = texta.encode('latin-1'),
            link = link.encode('latin-1'),
            hora = hora[-5:],
            ))
    return news

def andina_news(request):
    import simplejson
    data = simplejson.dumps(andina(), indent=2, ensure_ascii=True, encoding='utf-8')
    return HttpResponse(data,mimetype='application/json')

def index(request):    
    return render_to_response('andina.html', {}, context_instance=RequestContext(request),)
