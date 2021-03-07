from ListaDatosResultante import ListaDatosResultantes
class matriz:
    def __init__(self, nombre):
        self.nombre = nombre
        self.filas = None
        self.columnas = None
        self.datos = ListaDatosResultantes()
        self.grupos = ListaDatosResultantes()
        self.siguiente = None
        self.anterior = None