# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select, text
from .models import Usuario

def listar(request):
    conn = engine_accesos.connect()
    stmt = """
        SELECT U.id AS id, U.usuario AS usuario, A.momento AS momento, U.correo AS correo 
        FROM usuarios U INNER JOIN accesos A ON U.id = A.usuario_id 
        GROUP BY U.usuario ORDER BY U.id
    """
    return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def obtener_usuario_correo(request, usuario_id):
    conn = engine_accesos.connect()
    stmt = select([Usuario.usuario, Usuario.correo]).where(Usuario.id == usuario_id)
    temp = [dict(r) for r in conn.execute(stmt)]
    return HttpResponse(json.dumps(temp[0]))
