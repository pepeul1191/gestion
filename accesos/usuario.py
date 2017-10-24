# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select, text, and_
from .models import Usuario

def listar(request):
    if request.method == 'GET':
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
    if request.method == 'GET':
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
    if request.method == 'GET':
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


def nombre_repetido(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        usuario_id = data['id']
        usuario = data['usuario']
        rpta = 0

        if usuario_id == 'E':
            #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ?
            conn = engine_accesos.connect()
            stmt = select([Usuario]).where(Usuario.usuario == usuario).count()
            for r in conn.execute(stmt):
                rpta = r[0]
        else:
            #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ? AND id = ?
            conn = engine_accesos.connect()
            stmt = select([Usuario]).where(and_(Usuario.usuario == usuario, Usuario.id == usuario_id)).count()
            rpta = None
            for r in conn.execute(stmt):
                rpta = r[0]
            if rpta == 1:
                rpta = 0
            else:
                #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ?
                conn = engine_accesos.connect()
                stmt = select([Usuario]).where(Usuario.usuario == usuario).count()
                for r in conn.execute(stmt):
                    rpta = r[0]

        return HttpResponse(rpta)

def correo_repetido(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        usuario_id = data['id']
        correo = data['correo']
        rpta = 0

        if usuario_id == 'E':
            #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ?
            conn = engine_accesos.connect()
            stmt = select([Usuario]).where(Usuario.correo == correo).count()
            for r in conn.execute(stmt):
                rpta = r[0]
        else:
            #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ? AND id = ?
            conn = engine_accesos.connect()
            stmt = select([Usuario]).where(and_(Usuario.correo == correo, Usuario.id == usuario_id)).count()
            rpta = None
            for r in conn.execute(stmt):
                rpta = r[0]
            if rpta == 1:
                rpta = 0
            else:
                #SELECT COUNT(*) AS cantidad FROM usuarios WHERE usuario = ?
                conn = engine_accesos.connect()
                stmt = select([Usuario]).where(Usuario.correo == correo).count()
                for r in conn.execute(stmt):
                    rpta = r[0]

        return HttpResponse(rpta)