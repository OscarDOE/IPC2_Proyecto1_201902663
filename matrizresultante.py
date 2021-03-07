from ListaDatosResultante import ListaDatosResultantes
from listagrupos import ListaGrupos
class matriz:
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.filas = None
        self.columnas = columnas
        self.datos = ListaDatosResultantes()
        self.grupos = ListaGrupos()
        self.gruposexistentes = None
        self.siguiente = None
        self.anterior = None