# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Item

def listar(request, subtitulo_id):
	conn = engine_accesos.connect()
	stmt = select([Item]).where(Item.subtitulo_id == subtitulo_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))