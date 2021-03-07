from grupos import frecuenciables

class ListaGrupos:
    def __init__(self):
        self.primero = None

    def insertar(self,grupo,frecuencia):
        nuevo = frecuenciables(grupo, frecuencia)
        if self.primero is None:
            self.primero = nuevo
        else: 
            temporal = self.primero    
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo    
            nuevo.anterior = temporal            

    def mostrardatos(self):
        temporal = self.primero
        while temporal is not None:
            print("GRUPO:",temporal.grupo,"FRECUENCIA:",temporal.frecuencia)
            temporal = temporal.siguiente        