# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy.sql import select
from main.database import engine_libros
from .models import Categoria
from main.helper import Helper

def index(request):
	menu = [
		{'url' : 'accesos', 'nombre' : 'Accesos'},
        {'url' : 'libros', 'nombre' : 'Libros'},
    ]
	'''
	items = [
		{"subtitulo":"Usuarios","items":[{"item":"Listado","url":"accesos/usuarios"}]},{"subtitulo":"Menu","items":[{"item":"Listado","url":"accesos/menus"}]},{"subtitulo":"Acceso a Funciones","items":[{"url":"accesos/permisos","item":"Listado de permisos"},{"item":"Listado de roles","url":"accesos/roles"}]},{"subtitulo":"Logs","items":[{"item":"Logs de errores","url":"accesos/log/errores"},{"url":"accesos/log/accesos","item":"Logs de acceso"},{"item":"Logs de operaciones","url":"accesos/log/operaciones"}]}
	]
	'''
	items = [
		{"subtitulo":"Libros","items":[{"item":"Gestión de Categorías","url":"libros/#/categoria"},{"url":"libros/#/autor","item":"Gestión de Autores"},{"item":"Gestión de Libros","url":"libros/#"}]}
	]
	data = {'titulo_pagina' : 'Gestión de Libros', 'modulo' : 'Libros'}
	context = {'helper' : Helper(), 'data': json.dumps(data),'menu' : json.dumps(menu), 'items' : json.dumps(items)}
	return render(request, 'libros/index.html', context)

def rest(request):
	conn = engine_libros.connect()
	stmt = select([Categoria])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))