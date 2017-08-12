# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from main.database import Base

class Categoria(Base):
	__tablename__ = 'categorias'
	id = Column(Integer, primary_key=True)
	nombre = Column(String)