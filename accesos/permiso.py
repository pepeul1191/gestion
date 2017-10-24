# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json, traceback
from main.helper import Helper
from main.database import engine_accesos, session_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select, text
from .models import Permiso

def listar(request, sistema_id):
    if request.method == 'GET':
        conn = engine_accesos.connect()
        stmt = select([Permiso]).where(Permiso.sistema_id == sistema_id)
        return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def listar_asociados(request, sistema_id, rol_id):
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
            INNER JOIN roles_permisos RP ON P.id = RP.permiso_id
            WHERE RP.rol_id = :rol_id
            ) P
            ON T.id = P.id
        """
        return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt, {'sistema_id' : sistema_id, 'rol_id' : rol_id})]))

def guardar(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        nuevos = data['nuevos']
        editados = data['editados']
        eliminados = data['eliminados']
        sistema_id = data['extra']['sistema_id']
        array_nuevos = []
        rpta = None
        session = session_accesos()

        try:
            if len(nuevos) != 0:
                for nuevo in nuevos:
                    temp_id = nuevo['id']
                    nombre = nuevo['nombre']
                    llave = nuevo['llave']
                    s = Permiso(llave = llave, nombre = nombre, sistema_id = sistema_id)
                    session.add(s)
                    session.flush()
                    temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
                    array_nuevos.append(temp)
            if len(editados) != 0:
                for editado in editados:
                    session.query(Permiso).filter_by(id = editado['id']).update(editado)
            if len(eliminados) != 0:
                for id in eliminados:
                    session.query(Permiso).filter_by(id = id).delete()
            session.commit()
            rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los permisos', array_nuevos]}
        except Exception as e:
            session.rollback()
            rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de permisos', traceback.format_exc()]}

        return HttpResponse(json.dumps(rpta))