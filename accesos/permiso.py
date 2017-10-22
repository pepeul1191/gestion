# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select, text
from .models import Permiso

def listar(request, sistema_id):
	conn = engine_accesos.connect()
	stmt = select([Permiso]).where(Permiso.sistema_id == sistema_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def listar_asociados(request, sistema_id, rol_id):
	conn = engine_accesos.connect()
	#execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
	stmt = """
		SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe, T.llave AS llave FROM 
        (
            SELECT id, nombre, llave, 0 AS existe FROM permisos WHERE sistema_id = :sistema_id
        ) T
        LEFT JOIN
        (
            SELECT P.id, P.nombre,  P.llave, 1 AS existe  FROM permisos P 
            INNER JOIN roles_permisos RP ON P.id = RP.permiso_id
            WHERE RP.rol_id = :rol_id
        ) P
        ON T.id = P.id
    """
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt, {'sistema_id' : sistema_id, 'rol_id' : rol_id})]))