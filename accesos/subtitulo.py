# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json, traceback
from main.helper import Helper
from main.database import engine_accesos, session_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Subtitulo

def listar(request, modulo_id):
	if request.method == 'GET':
		conn = engine_accesos.connect()
		stmt = select([Subtitulo]).where(Subtitulo.modulo_id == modulo_id)
		return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def guardar(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        nuevos = data['nuevos']
        editados = data['editados']
        eliminados = data['eliminados']
        modulo_id = data['extra']['id_modulo']
        array_nuevos = []
        rpta = None
        session = session_accesos()

        try:
            if len(nuevos) != 0:
                for nuevo in nuevos:
                    temp_id = nuevo['id']
                    nombre = nuevo['nombre']
                    s = Subtitulo(nombre = nombre, modulo_id = modulo_id)
                    session.add(s)
                    session.flush()
                    temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
                    array_nuevos.append(temp)
            if len(editados) != 0:
                for editado in editados:
                    id = editado['id']
                    nombre = editado['nombre']
                    session.query(Subtitulo).filter_by(id = id).update(editado)
            if len(eliminados) != 0:
                for id in eliminados:
                    session.query(Subtitulo).filter_by(id = id).delete()
            session.commit()
            rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los subtitulos', array_nuevos]}
        except Exception as e:
            session.rollback()
            rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de subtitulos', traceback.format_exc()]}

        return HttpResponse(json.dumps(rpta))