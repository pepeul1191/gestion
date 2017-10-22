# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from main.database import Base
# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html
class EstadoUsuario(Base):
	__tablename__ = 'estado_usuario'
	id = Column(Integer, primary_key = True)
	nombre = Column(String)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key = True)
    usuario = Column(String)
    contrasenia = Column(String)
    correo = Column(String)
    estado_usuario_id = Column(Integer, ForeignKey('estado_usuario.id'))

class Sistema(Base):
    __tablename__ = 'sistemas'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    version = Column(String)
    repositorio = Column(String)

class Modulo(Base):
    __tablename__ = 'modulos'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    url = Column(String)
    sistema_id = Column(Integer, ForeignKey('sistemas.id'))
    
class Subtitulo(Base):
    __tablename__ = 'subtitulos'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    modulo_id = Column(Integer, ForeignKey('modulos.id'))
    
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key = True)
    nombre = Column(String)
    url = Column(String)
    subtitulo_id = Column(Integer, ForeignKey('subtitulos.id'))
    