#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LATEST NEWS FROM ANDINA
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from lxml.html import parse
from lxml import etree
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext
from django.utils.encoding import smart_unicode, force_unicode
import simplejson
from django.template.defaultfilters import slugify, truncatewords, join

def andina():
    url = 'http://www.andina.com.pe/Espanol/aspa2012/index.aspx'
    root = parse(url).getroot()
    news = []    
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

def presidencia_noticias_otro():
    url = 'http://www.presidencia.gob.pe'
    root = parse(url).getroot()
    news = []    
    noticias = root.xpath("//div[@class='nsp_art']")    
    for noticia in noticias:
        news.append(dict(
            titular = noticia.xpath("div/h4/a")[0].text_content(),
            link = u'%s%s' %('http://presidencia.gob.pe',
                noticia.xpath("div/h4/a/@href")[0]),
            descripcion = noticia.xpath("div/p")[0].text_content(),
            ))
    return news

def presidencia_noticias():
    """
    ?limitstart=5
    Limita de 5 en 5 los discursos servira para que en el json se vayan recuperando
    en base a esa cantidad.
    """    
    url = 'http://www.presidencia.gob.pe/ollanta/blog'
    root = parse(url).getroot()
    news = []    
    discursos = root.xpath("//div[@class='entryContent entry']")
    for discurso in discursos:
        descripcion = join(['<p>'+p.text_content()+'</p>'
            for p in discurso.xpath(
            "div[@class='entry-body']")[0].xpath(
            "p[@style='text-align: justify;']")],'')
        news.append(dict(
            titular = discurso.xpath("h2")[0].text_content(),
            link = u'%s%s' % ('http://presidencia.gob.pe/',
                slugify(discurso.xpath("h2")[0].text_content())),
            descripcion = descripcion,
            ))    
    return news

def presidencia_discursos():
    """
    ?limitstart=5
    Limita de 5 en 5 los discursos servira para que en el json se vayan recuperando
    en base a esa cantidad.
    """    
    url = 'http://www.presidencia.gob.pe/discursos-del-presidente/blog'
    root = parse(url).getroot()
    news = []    
    discursos = root.xpath("//div[@class='entryContent entry']")
    for discurso in discursos:
        descripcion = truncatewords(join(['<p>'+p.text_content()+'</p>'
            for p in discurso.xpath(
            "div[@class='entry-body']")[0].xpath(
            "p[@style='text-align: justify;']")],''),30)
        news.append(dict(
            titular = discurso.xpath("h2")[0].text_content(),
            link = u'%s%s' % ('http://presidencia.gob.pe/',
                slugify(discurso.xpath("h2")[0].text_content())),
            descripcion = descripcion,
            ))    
    return news

def andina_news(request):    
    data = simplejson.dumps(andina(), indent=2, ensure_ascii=True, encoding='utf-8')
    data = 'callback('+data+');'
    return HttpResponse(data,mimetype='application/json')

def presidencia_noticias_news(request):
    data = simplejson.dumps(presidencia_noticias(),
        indent=2, ensure_ascii=True, encoding='utf-8')
    data = 'ver_noticias('+data+');'
    return HttpResponse(data,mimetype='application/json')

def presidencia_discursos_news(request):
    data = simplejson.dumps(presidencia_discursos(),
        indent=2, ensure_ascii=True, encoding='utf-8')
    data = 'ver_discursos('+data+');'
    return HttpResponse(data,mimetype='application/json')

def index(request):    
    return render_to_response('andina.html', {}, context_instance=RequestContext(request),)

