from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from bd.configuracionbd import BaseDatos


class Actividad(BaseDatos):

    __tablename__ = 'actividad'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    terminada = Column(Boolean)
    viajeros = relationship("Viajero")
    ordename = Column(Integer, ForeignKey('ordename.id'))
    gastos = relationship("Gasto")

    def __init__(self, nombre, terminada, ordename):
        self.nombre = nombre
        self.terminada = terminada
        self.ordename = ordename
        self.viajeros = []
        self.gastos = []

    def __str__(self):
        return self.nombre

    def distribuir_gastos(self):
        distribucion = []
        gastos_por_viajero = []
        if self.gastos:
            gastos_por_viajero = self.gastos_por_viajero()

            if len(gastos_por_viajero) == 1:
                distribucion.append([gastos_por_viajero[0][0],gastos_por_viajero[0][0], gastos_por_viajero[0][1], 0.0])
                distribucion.append([gastos_por_viajero[0][0], gastos_por_viajero[0][0], gastos_por_viajero[0][1], 0.0])
            elif len(gastos_por_viajero) == 2:
                total_gastos = gastos_por_viajero[0][1] + gastos_por_viajero[1][1]
                gastos_por_persona = total_gastos /2
                if gastos_por_persona > gastos_por_viajero[0][1]:
                    distribucion.append(
                        [gastos_por_viajero[0][0], gastos_por_viajero[1][0], gastos_por_viajero[0][1], gastos_por_persona - gastos_por_viajero[0][1]])
                    distribucion.append(
                        [gastos_por_viajero[1][0], gastos_por_viajero[1][0], gastos_por_viajero[1][1], 0.0])
                else:
                    distribucion.append(
                        [gastos_por_viajero[0][0], gastos_por_viajero[0][0], gastos_por_viajero[0][1], 0.0])
                    distribucion.append(
                        [gastos_por_viajero[1][0], gastos_por_viajero[0][0], gastos_por_viajero[1][1], gastos_por_persona - gastos_por_viajero[1][1]])
            else:
                distribucion = self.repartir_gastos(gastos_por_viajero)


        return distribucion

    def gastos_por_viajero(self):
        gastos_por_viajero = []
        if self.gastos:
            for viajero in self.viajeros:
                gasto_viajero = 0.0
                for gasto in self.gastos:
                    if viajero == gasto.viajero:
                        gasto_viajero = gasto_viajero + gasto.valor

                gastos_por_viajero.append([viajero, gasto_viajero])

        return gastos_por_viajero

    def repartir_gastos(self, gastos_por_viajero):
        total_gastos = 0
        gastos_por_persona = 0
        distribucion = []

        for gasto in gastos_por_viajero:
            total_gastos = total_gastos + gasto[1]

        gastos_por_persona = total_gastos / len(gastos_por_viajero)

        #Primero se establece a quienes les deben y cuanto
        for gasto in gastos_por_viajero:
            if(gasto[1]>=gastos_por_persona):
                distribucion.append([gasto[0], gasto[0], gasto[1], gasto[1] - gastos_por_persona])

        #Luego, quienes deben pagan hasta quedar sin deuda
        for gasto in gastos_por_viajero:
            if gasto[1]<gastos_por_persona:
                dinero_por_pagar = gastos_por_persona - gasto[1]
                for ledeben in distribucion:
                    if dinero_por_pagar>0:
                        if dinero_por_pagar <= ledeben[3]:
                            distribucion.append([gasto[0], ledeben[0], gasto[1], dinero_por_pagar])
                            ledeben[3] = ledeben[3] - dinero_por_pagar
                            dinero_por_pagar = 0
                        else:
                            distribucion.append([gasto[0], ledeben[0], gasto[1], ledeben[3]])
                            dinero_por_pagar = dinero_por_pagar - ledeben[3]
                            ledeben[3] =0
        return distribucion



