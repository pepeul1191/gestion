# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from main.database import Base
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
class Categoria(Base):
	__tablename__ = 'categorias'
	id = Column(Integer, primary_key = True)
	nombre = Column(String)

class Autor(Base):
	__tablename__ = 'autores'
	id = Column(Integer, primary_key = True)
	nombre = Column(String)

class Extension(Base):
	__tablename__ = 'extensiones'
	id = Column(Integer, primary_key = True)
	nombre = Column(String)

class Documento(Base):
	__tablename__ = 'documentos'
	id = Column(Integer, primary_key = True)
	titulo = Column(String)
	paginas = Column(Integer)
	extension_id = Column(Integer, ForeignKey('extension.id'))

documentos_categorias = Table('documentos_categorias', Base.metadata,
    Column('documento_id', Integer, ForeignKey('documento.id')),
    Column('categoria_id', Integer, ForeignKey('categoria.id'))
)

documentos_autores = Table('documentos_autores', Base.metadata,
    Column('documento_id', Integer, ForeignKey('documento.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)