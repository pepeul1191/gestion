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

class Libro(Base):
	__tablename__ = 'libros'
	id = Column(Integer, primary_key = True)
	titulo = Column(String)
	paginas = Column(Integer)
	extension_id = Column(Integer, ForeignKey('extension.id'))

libros_categorias = Table('libros_categorias', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('categoria_id', Integer, ForeignKey('categoria.id'))
)

libros_autores = Table('libros_autores', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)