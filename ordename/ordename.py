from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from bd.configuracionbd import BaseDatos


class Ordename(BaseDatos):

    __tablename__ = 'ordename'
    id = Column(Integer, primary_key=True)
    viajeros = relationship("Viajero")

    def __init__(self):
        self.viajeros = []

    def __str__(self):
        return self.id
