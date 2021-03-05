from datos import posicion

class ListaDatos:
    def __init__(self):
        self.primero = None

    def insertar(self,x, y, valor,filas, columnas, nombrematriz):
        nuevo = posicion(x,y,valor,filas,columnas, nombrematriz)
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

    def getNodoDatos(self, nombrematriz):
        temporal = self.primero
        while temporal is not None:
            if str.lower(temporal.nombrematriz) == str.lower(nombrematriz):
                return temporal
            temporal = temporal.siguiente
        return None

    def gettotal(self):
        temporal = self.primero
        contador = 0
        while temporal is not None:
            contador += 1
            temporal = temporal.siguiente
        return contador   

    def recorrer (self, hasta):
        temporal = self.primero
        i = 0
        while i <= hasta:
            if i == hasta:
                return temporal
            temporal = temporal.siguiente

    def recorrercadam(self, hasta, columnas,filas_pasada):
        temporal = self.primero
        z = 0
        while temporal is not None:
            for filas in range(filas_pasada+1):
                if filas == 0:
                    return temporal.valor
                elif z == (0+(filas_pasada*columnas)):
                    return temporal.valor
                else:
                    temporal.siguiente  
                    z += 1  
    def recorrercadan(self,pasadas):
        temporal = self.primero
        c = 0
        while temporal is not None:
            if c == pasadas:
                return temporal.valor
            else:
                c += 1
            temporal = temporal.siguiente    
#C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\y.xml
    def recorrerm (self,columna_va, filas_va,columnas):
        temporal = self.primero
        c = 0
        count = 0
        while temporal is not None:
            if count != columna_va:
                temporal = temporal.siguiente
                count += 1
            if filas_va == c:
                return temporal.valor
            else:
                c += 1
            temporal = temporal.siguiente   


            '''if hasta == 0:
                return temporal.valor

            elif hasta % columnas == 0:
                return 1
            temporal = temporal.siguiente'''

    '''def recorrerNodos(self):
        temporal =     '''

    '''def compararfilas(self):
        temporal = self.primero
        while temporal is not None:
            fila_actual = temporal.x
            if fila_actual == temporal.x'''
