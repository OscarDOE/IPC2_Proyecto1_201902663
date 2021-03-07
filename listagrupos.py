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

    def mensajexml(self):
        print("-------------------------------------------GRUPOS----------------------------------")
        temporal = self.primero
        #m = mensaje
        a = ""
        while temporal is not None:
            #print("LLEGO A GRUPOS")
            #print("X:",temporal.x, "Y:", temporal.y, "VALOR:",temporal.valor, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas)
            a += "        <Frecuencia g=\""+str(temporal.grupo)+"\">"+str(temporal.frecuencia)+"</Frecuencia>\n"
            temporal = temporal.siguiente     
        return a 