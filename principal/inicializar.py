from ordename.ordename import Ordename
from ordename.viajero import Viajero
from ordename.actividad import Actividad
from ordename.gasto import Gasto
from datetime import date
from bd.configuracionbd import BaseDatos, engine, Session

if __name__ == '__main__':
    #Crea la BD
    BaseDatos.metadata.create_all(engine)

    #Abre la sesión
    session = Session()

    #Crear ordename
    ordename = Ordename()

    #crear viajeros
    viajero1 = Viajero(nombre="Rubby", apellido="Casallas Gutiérrez", correo="rcasalla@uniandes.edu.co", ordename=ordename)
    viajero2 = Viajero(nombre="Gloria", apellido="Cortés Buitrago", correo="gcortes@uniandes.edu.co", ordename=ordename)
    ordename.viajeros = [viajero1, viajero2]

    #crear actividad
    actividad = Actividad(nombre="Paseo a Neusa", terminada=False, ordename=ordename)
    actividad.viajeros = [viajero1, viajero2]
    ordename.actividades = [actividad]

    #crear gastos
    gasto1 = Gasto(concepto="Gasolina", valor=80000.0, fecha = date(2021, 2, 10), viajero=viajero1, actividad=actividad)
    gasto2 = Gasto(concepto="Peaje autopista", valor=10000.0, fecha = date(2021, 2, 10), viajero=viajero1, actividad=actividad)
    gasto3 = Gasto(concepto="Peaje Ubate", valor=10000.0, fecha = date(2021, 2, 10), viajero=viajero2, actividad=actividad)
    actividad.gastos = [gasto1, gasto2, gasto3]

    session.add(viajero1)
    session.add(viajero2)
    session.add(ordename)
    session.add(actividad)
    session.add(gasto1)
    session.add(gasto2)
    session.add(gasto3)
    session.close()

