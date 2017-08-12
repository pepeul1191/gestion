# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Categoria

def index(request):
	r = serialize('json', Categoria.objects.all())
	return HttpResponse(r)