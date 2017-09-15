# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from main.helper import Helper

def index(request):
	data = {"mensaje" : False}
	context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
	return render(request, 'login/index.html', context)