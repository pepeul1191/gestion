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
    nombre = Column(String)
    contrasenia = Column(String)
    correo = Column(String)
    estado_usuario_id = Column(Integer, ForeignKey('estado_usuario.id'))