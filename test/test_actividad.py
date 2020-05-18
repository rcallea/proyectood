from datetime import date
from unittest import TestCase

from ordename.actividad import Actividad
from ordename.gasto import Gasto
from ordename.ordename import Ordename
from ordename.viajero import Viajero


class TestActividad(TestCase):
    def setUp(self):
        self.ordename = Ordename()
        #crear viajeros
        self.viajero1 = Viajero(nombre="Rubby", apellido="Casallas Gutiérrez", correo="rcasalla@uniandes.edu.co", ordename=self.ordename)
        self.viajero2 = Viajero(nombre="Gloria", apellido="Cortés Buitrago", correo="gcortes@uniandes.edu.co", ordename=self.ordename)
        self.viajero3 = Viajero(nombre="Juan Pablo", apellido="Gomez Reyes", correo="jp.reyes@uniandes.edu.co", ordename=self.ordename)
        self.ordename.viajeros = [self.viajero1, self.viajero2, self.viajero3]

        #crear actividad
        self.actividad = Actividad(nombre="Paseo a Neusa", terminada=False, ordename=self.ordename)
        self.actividad.viajeros = [self.viajero1, self.viajero2]
        self.ordename.actividades = [self.actividad]



    def test_sin_gastos(self):
        resultados = self.actividad.distribuir_gastos()
        self.assertEqual(resultados, [])

    def test_gastos_una_unica_persona(self):
        self.gasto1 = Gasto(concepto="Gasolina", valor=80000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.gasto2 = Gasto(concepto="Peaje autopista", valor=10000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.actividad.gastos = [self.gasto1, self.gasto2]

        resultados = self.actividad.distribuir_gastos()
        self.assertEqual(resultados[0], [self.viajero1, self.viajero1, 90000.0, 0.0])

    def test_gastos_dos_personas(self):
        self.gasto1 = Gasto(concepto="Gasolina", valor=80000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.gasto2 = Gasto(concepto="Peaje autopista", valor=10000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.gasto3 = Gasto(concepto="Peaje Ubate", valor=10000.0, fecha = date(2021, 2, 10), viajero=self.viajero2, actividad=self.actividad)
        self.actividad.gastos = [self.gasto1, self.gasto2, self.gasto3]

        resultados = self.actividad.distribuir_gastos()
        self.assertEqual(resultados[0], [self.viajero1, self.viajero1, 90000.0, 0.0])
        self.assertEqual(resultados[1], [self.viajero2, self.viajero1, 10000.0, 40000.0])

    def test_gastos_n_personas(self):
        self.gasto1 = Gasto(concepto="Gasolina", valor=80000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.gasto2 = Gasto(concepto="Peaje autopista", valor=10000.0, fecha = date(2021, 2, 10), viajero=self.viajero1, actividad=self.actividad)
        self.gasto3 = Gasto(concepto="Peaje Ubate", valor=10000.0, fecha = date(2021, 2, 10), viajero=self.viajero2, actividad=self.actividad)
        self.gasto4 = Gasto(concepto="Frutas", valor=20000.0, fecha = date(2021, 2, 10), viajero=self.viajero3, actividad=self.actividad)
        self.actividad.gastos = [self.gasto1, self.gasto2, self.gasto3, self.gasto4]
        self.actividad.viajeros.append(self.viajero3)

        resultados = self.actividad.distribuir_gastos()
        print(resultados)
        self.assertEqual(resultados[0], [self.viajero1, self.viajero1, 90000.0, 0.0])
        self.assertEqual(resultados[1], [self.viajero2, self.viajero1, 10000.0, 30000.0])
        self.assertEqual(resultados[2], [self.viajero3, self.viajero1, 20000.0, 20000.0])
