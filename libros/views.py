# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from sqlalchemy.sql import select
from main.database import engine
from .models import Categoria

def index(request):
	conn = engine.connect()
	stmt = select([Categoria])
	return HttpResponse(json.dumps([dict(r) for r in conn.execute(stmt)]))