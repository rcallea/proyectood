from sqlalchemy import Column, Integer, String, ForeignKey
from bd.configuracionbd import BaseDatos


class Viajero(BaseDatos):

    __tablename__ = 'viajero'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String)
    ordename = Column(Integer, ForeignKey('ordename.id'))
    actividad = Column(Integer, ForeignKey('actividad.id'))

    def __init__(self, nombre, apellido, correo, ordename):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.ordename = ordename

    def __str__(self):
        return self.nombre + " " + self.apellido + " (" + self.correo + ")"

    def __eq__(self, otro_viajero):
        if not isinstance(otro_viajero, Viajero):
            return NotImplemented

        return self.id == otro_viajero.id and self.nombre == otro_viajero.nombre and self.apellido == otro_viajero.apellido and self.correo == otro_viajero.correo
