# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from main.helper import Helper

def index(request):
	menu = [
		{'url' : 'accesos', 'nombre' : 'Accesos'},
        {'url' : 'libros', 'nombre' : 'Libros'},
    ]
	items = [{"subtitulo":"","items":[{"item":"Gestión de Sistemas","url":"accesos/#/sistema"},{"item":"Gestión de Usuarios","url":"accesos/#/usuario"}]}]
	data = {'titulo_pagina' : 'Gestión Accesos', 'modulo' : 'Accesos'}
	context = {'helper' : Helper(), 'data': json.dumps(data),'menu' : json.dumps(menu), 'items' : json.dumps(items)}

	return render(request, 'accesos/index.html', context)