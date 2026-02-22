from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contacto(Base):
    __tablename__ = "contactos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    mensagem = Column(Text)
    criado_em = Column(DateTime, default=datetime.utcnow)
