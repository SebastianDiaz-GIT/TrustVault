from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class PasswordEntry(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, unique=True, index=True)
    username = Column(String)
    password = Column(String)  # Se guardará cifrado
