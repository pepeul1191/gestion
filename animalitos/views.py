# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from main.helper import Helper

def index(request):
	menu = [
				 {'url' : '#/', 'nombre' : 'Home'},
             {'url' : '#/buscar', 'nombre' : 'Buscar'},
             {'url' : '#/contacto', 'nombre' : 'Contacto'}
      ]
	data = ''
	context = {'helper' : Helper(), 'data': data,'menu' : json.dumps(menu)}
	return render(request, 'animalitos/index.html', context)