from listadatos import ListaDatos
class matriz:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.datos = ListaDatos()
        self.siguiente = None