# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Subtitulo

def listar(request, modulo_id):
	conn = engine_accesos.connect()
	stmt = select([Subtitulo]).where(Subtitulo.modulo_id == modulo_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))