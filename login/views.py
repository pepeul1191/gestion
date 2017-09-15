# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sqlalchemy.sql import select, and_, func
from main.helper import Helper
from main.cipher import decode, encode
from main.database import engine_accesos
from accesos.models import Usuario

def index(request):
    if request.method == 'GET':
        data = {'mensaje' : False}
        context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
        return render(request, 'login/index.html', context)
    else:
        return redirect(Helper().get('BASE_URL') + 'error/access/404')

def acceder(request):
    if request.method == 'POST':
        usuario =request.POST.get('usuario')
        contrasenia = request.POST.get('contrasenia')

        conn = engine_accesos.connect()
        stmt = select([Usuario]).where(and_(Usuario.usuario == usuario, Usuario.contrasenia == encode(contrasenia))).count()
        rpta = None
        for r in conn.execute(stmt):
            rpta = r[0]

        if int(rpta) == 1:
            return redirect(Helper().get('BASE_URL') + 'libros')
        else:
            data = {'mensaje' : True}
            context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
            return render(request, 'login/index.html', context)
    else:
        return redirect(Helper().get('BASE_URL') + 'error/access/404')