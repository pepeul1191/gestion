# main/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine_libros = create_engine('sqlite:///db/db_libros.db')
engine_accesos = create_engine('sqlite:///db/db_accesos.db')