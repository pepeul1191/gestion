# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json, traceback
from main.helper import Helper
from main.database import engine_accesos, session_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Sistema

def listar(request):
    if request.method == 'GET':
        conn = engine_accesos.connect()
        stmt = select([Sistema])
        return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def usuario(request, usuario_id):
    if request.method == 'GET':
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

def guardar(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        nuevos = data['nuevos']
        editados = data['editados']
        eliminados = data['eliminados']
        array_nuevos = []
        rpta = None
        session = session_accesos()

        try:
            if len(nuevos) != 0:
                for nuevo in nuevos:
                    temp_id = nuevo['id']
                    nombre = nuevo['nombre']
                    version = nuevo['version']
                    repositorio = nuevo['repositorio']
                    s = Sistema(nombre = nombre, version = version, repositorio = repositorio)
                    session.add(s)
                    session.flush()
                    temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
                    array_nuevos.append(temp)
            if len(editados) != 0:
                for editado in editados:
                    id = editado['id']
                    nombre = editado['nombre']
                    version = editado['version']
                    repositorio = editado['repositorio']
                    session.query(Sistema).filter_by(id = id).update(editado)
            if len(eliminados) != 0:
                for id in eliminados:
                    session.query(Sistema).filter_by(id = id).delete()
            session.commit()
            rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los sistemas', array_nuevos]}
        except Exception as e:
            session.rollback()
            rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de sistemas', traceback.format_exc()]}

        return HttpResponse(json.dumps(rpta))