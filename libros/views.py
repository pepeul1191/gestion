# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sqlalchemy.sql import select
from main.database import engine_libros
from .models import Categoria, Autor
from main.helper import Helper

def index(request):
	menu = [
		{'url' : 'accesos', 'nombre' : 'Accesos'},
        {'url' : 'libros', 'nombre' : 'Libros'},
    ]
	items = [
		{"subtitulo":"Libros","items":[{"item":"Gestión de Categorías","url":"libros/#/categoria"},{"url":"libros/#/autor","item":"Gestión de Autores"},{"item":"Gestión de Libros","url":"libros/#"}]}
	]
	data = {'titulo_pagina' : 'Gestión de Libros', 'modulo' : 'Libros'}
	context = {'helper' : Helper(), 'data': json.dumps(data),'menu' : json.dumps(menu), 'items' : json.dumps(items)}
	return render(request, 'libros/index.html', context)

def autor_guardar(request):
	if request.method == 'POST':
		data =json.loads(request.POST.get('data'))
		nuevos = data['nuevos']
        editados = data['editados']
        eliminados = data['eliminados']

		try:
			if len(nuevos) != 0:
				list_nuevos = []
				for i in nuevos:
					'crear'
			if len(editados) != 0:
				for i in editados:
					'editar'
			if len(eliminados) != 0:
				for i in eliminados:
					'eliminar'
					#session.query(User).filter(User.id==7).delete()
		except Exception as e:
			rpta = { 'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de criticidades', e] }

		return HttpResponse(json.dumps(rpta))
	else:
		return redirect(Helper().get('BASE_URL') + 'error/access/404')
	
def autor_listar(request):
	conn = engine_libros.connect()
	stmt = select([Autor])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def categoria_listar(request):
	conn = engine_libros.connect()
	stmt = select([Categoria])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))