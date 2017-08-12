# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
	class Meta:
		db_table = 'categorias'
	nombre = models.CharField(max_length=25)