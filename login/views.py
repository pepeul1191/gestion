# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from main.helper import Helper

def index(request):
	data = ''
	context = {'helper' : Helper(), 'data': data,'menu' : '', 'items' : ''}
	return render(request, 'login/index.html', context)