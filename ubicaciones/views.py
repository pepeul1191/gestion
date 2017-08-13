# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy.sql import select
from main.database import engine_ubicaciones
from .models import Departamento, Provincia, Distrito, VWDistritoProvinciaDepartamento as VW

def vw_distrito_provincia_departamento_buscar(request):
	conn = engine_ubicaciones.connect()
	stmt = select([VW]).where(VW.nombre.like(request.GET.get('nombre') + '%' )).limit(10)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def departamento_listar(request):
	conn = engine_ubicaciones.connect()
	stmt = select([Departamento])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def provincia_listar(request, departamento_id):
	conn = engine_ubicaciones.connect()
	stmt = select([Provincia.id, Provincia.nombre]).where(Provincia.departamento_id == departamento_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def distrito_listar(request, provincia_id):
	conn = engine_ubicaciones.connect()
	stmt = select([Distrito]).where(Distrito.provincia_id == provincia_id)
	rpta = []
	for r in conn.execute(stmt):
		rpta.append({'id':r[0], 'nombre':str(r[1])})
	return HttpResponse(json.dumps(rpta))