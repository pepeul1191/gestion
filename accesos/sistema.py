# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from main.helper import Helper
from main.database import engine_accesos
from django.http import HttpResponse
from sqlalchemy.sql import select
from .models import Sistema

def listar(request):
	conn = engine_accesos.connect()
	stmt = select([Sistema])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))