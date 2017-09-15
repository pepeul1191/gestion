# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.helper import Helper

def index(request):
    if request.method == 'GET':
        data = {"mensaje" : False}
        context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
        return render(request, 'login/index.html', context)
    else:
        return redirect(Helper().get("BASE_URL") + "error/404")

def acceder(request):
    if request.method == 'POST':
        data = {"mensaje" : True}
        context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
        return render(request, 'login/index.html', context)
    else:
        return redirect(Helper().get("BASE_URL") + "error/404")