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

def listar_permisos(request, sistema_id, usuario_id):
    conn = engine_accesos.connect()
    stmt = """
        SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe, T.llave AS llave FROM
        (
            SELECT id, nombre, llave, 0 AS existe FROM permisos WHERE sistema_id = :sistema_id
        ) T
        LEFT JOIN
        (
            SELECT P.id, P.nombre,  P.llave, 1 AS existe  FROM permisos P 
            INNER JOIN usuarios_permisos UP ON P.id = UP.permiso_id
            WHERE UP.usuario_id = :usuario_id
        ) P
        ON T.id = P.id
    """
    return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt, {'sistema_id' : sistema_id, 'usuario_id' : usuario_id})]))


def listar_roles(request, sistema_id, usuario_id):
    conn = engine_accesos.connect()
    stmt = """
        SELECT T.id AS id, T.nombre AS nombre, (CASE WHEN (P.existe = 1) THEN 1 ELSE 0 END) AS existe FROM
        (
            SELECT id, nombre, 0 AS existe FROM roles WHERE sistema_id = :sistema_id
        ) T
        LEFT JOIN
        (
            SELECT R.id, R.nombre, 1 AS existe  FROM roles R 
            INNER JOIN usuarios_roles UR ON R.id = UR.rol_id
            WHERE UR.usuario_id = :usuario_id
        ) P
        ON T.id = P.id
    """
    return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt, {'sistema_id' : sistema_id, 'usuario_id' : usuario_id})]))
