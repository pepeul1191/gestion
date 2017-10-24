# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json, traceback
from main.helper import Helper
from main.database import engine_accesos, session_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Item

def listar(request, subtitulo_id):
	conn = engine_accesos.connect()
	stmt = select([Item]).where(Item.subtitulo_id == subtitulo_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))

def guardar(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        nuevos = data['nuevos']
        editados = data['editados']
        eliminados = data['eliminados']
        subtitulo_id = data['extra']['id_subtitulo']
        array_nuevos = []
        rpta = None
        session = session_accesos()

        try:
            if len(nuevos) != 0:
                for nuevo in nuevos:
                    temp_id = nuevo['id']
                    nombre = nuevo['nombre']
                    url = nuevo['url']
                    s = Item(nombre = nombre, url = url, subtitulo_id = subtitulo_id)
                    session.add(s)
                    session.flush()
                    temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
                    array_nuevos.append(temp)
            if len(editados) != 0:
                for editado in editados:
                    id = editado['id']
                    nombre = editado['nombre']
                    session.query(Item).filter_by(id = id).update(editado)
            if len(eliminados) != 0:
                for id in eliminados:
                    session.query(Item).filter_by(id = id).delete()
            session.commit()
            rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los items', array_nuevos]}
        except Exception as e:
            session.rollback()
            rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de item', traceback.format_exc()]}

        return HttpResponse(json.dumps(rpta))