# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from main.database import Base
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
class Departamento(Base):
	__tablename__ = 'departamentos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String)

class Provincia(Base):
	__tablename__ = 'provincias'
	id = Column(Integer, primary_key=True)
	nombre = Column(String)
	departamento_id = Column(Integer, ForeignKey('departamento.id'))

class Distrito(Base):
	__tablename__ = 'distritos'
	id = Column(Integer, primary_key=True)
	nombre = Column(String)
	provincia_id = Column(Integer, ForeignKey('provincia.id'))

class VWDistritoProvinciaDepartamento(Base):
	__tablename__ = 'vw_distrito_provincia_departamento'
	id = Column(Integer, primary_key=True)
	nombre = Column(String)