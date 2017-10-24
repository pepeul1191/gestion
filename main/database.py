# main/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine_libros = create_engine('sqlite:///db/db_libros.db')
session_libros = sessionmaker()
session_libros.configure(bind=engine_libros)

engine_accesos = create_engine('sqlite:///db/db_accesos.db')
session_accesos = sessionmaker()
session_accesos.configure(bind=engine_accesos)