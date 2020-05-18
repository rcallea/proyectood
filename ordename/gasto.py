from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from bd.configuracionbd import BaseDatos


class Gasto(BaseDatos):
    __tablename__ = 'gasto'
    id = Column(Integer, primary_key=True)
    concepto = Column(String)
    valor = Column(Float)
    fecha = Column(Date)
    viajero = Column(Integer, ForeignKey("viajero.id"))
    actividad = Column(Integer, ForeignKey('actividad.id'))

    def __init__(self, concepto, valor, fecha, viajero, actividad):
        self.concepto = concepto
        self.valor = valor
        self.fecha = fecha
        self.viajero = viajero
        self.actividad = actividad

    def __str__(self):
        return self.nombre + " " + self.apellido + " (" + self.correo + ")"
