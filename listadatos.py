from datos import posicion

class ListaDatos:
    def __init__(self):
        self.primero = None

    def insertar(self,x, y, valor,filas, columnas):
        nuevo = posicion(x,y,valor,filas,columnas)
        if self.primero is None:
            self.primero = nuevo
        else: 
            temporal = self.primero    
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo 
    
    def mostrardatos(self):
        temporal = self.primero
        while temporal is not None:
            print("X:",temporal.x, "Y:", temporal.y, "VALOR:",temporal.valor, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas)
            temporal = temporal.siguiente

    def getNodoDatos(self, valor):
        temporal = self.primero
        while temporal is not None:
            if str.lower(temporal.x) == str.lower(valor):
                return temporal
            temporal = temporal.siguiente
        return None

    '''def recorrerNodos(self):
        temporal =     '''

    '''def compararfilas(self):
        temporal = self.primero
        while temporal is not None:
            fila_actual = temporal.x
            if fila_actual == temporal.x'''
