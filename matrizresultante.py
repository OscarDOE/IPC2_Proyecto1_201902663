from ListaDatosResultante import ListaDatosResultantes
class matriz:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.datos = ListaDatos()
        self.grupos = ListaDatos()
        self.siguiente = None
        self.anterior = None