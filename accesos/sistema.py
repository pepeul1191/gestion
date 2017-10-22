# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Sistema

def listar(request):
	conn = engine_accesos.connect()
	stmt = select([Sistema])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def usuario(request, usuario_id):
	conn = engine_accesos.connect()
	stmt = """
		SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe FROM
        (
            SELECT id, nombre, 0 AS existe FROM sistemas
        ) T
        LEFT JOIN
        (
            SELECT S.id, S.nombre, 1 AS existe FROM sistemas S
            INNER JOIN usuarios_sistemas US ON US.sistema_id = S.id
            WHERE US.usuario_id = :usuario_id
        ) P
        ON T.id = P.id
    """
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt, {'usuario_id' : usuario_id})]))