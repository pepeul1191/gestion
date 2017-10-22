# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Modulo

def listar(request, sistema_id):
	conn = engine_accesos.connect()
	stmt = select([Modulo]).where(Modulo.sistema_id == sistema_id)
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))