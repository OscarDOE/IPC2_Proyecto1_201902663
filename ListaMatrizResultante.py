from matrizresultante import matriz

class ListaMatricesResultantes:
    def __init__(self):
        self.primero = None


    def insertar(self,nombre, columnas):
        nuevo = matriz(nombre, columnas)
        if self.primero is None:
            self.primero = nuevo
        else: 
            temporal = self.primero    
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo 
            nuevo.anterior = temporal
    #C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\x.xml
    #C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\y.xml
    def mostrardatos(self):
        temporal = self.primero
        while temporal is not None:
            print("NOMBRE:",temporal.nombre, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas,"GRUPOS:",temporal.gruposexistentes)
            print("-----------------DATOS-------------------")
            if(temporal.datos.mostrardatos() != None):
                print(temporal.datos.mostrardatos())
            if (temporal.grupos.mostrardatos() != None):
                print(temporal.grupos.mostrardatos())    
            print("-----------------------------------------")
            #while tmp is not None:
             #   print("X:",tmp.datos.)
            temporal = temporal.siguiente

    def getNodoMatriz(self, valor):
        temporal = self.primero
        while temporal is not None:
            if str.lower(temporal.nombre) == str.lower(valor):
                return temporal
            temporal = temporal.siguiente
        return None    

    def getcantidad(self):
        temporal = self.primero
        contador = 0
        while temporal is not None:
            contador += 1
            temporal = temporal.siguiente
        return contador 
        #ESPECIFICOS

    def mostrarnombresmatrices(self):
        temporal = self.primero
        while temporal is not None:
            print("NOMBRE:",temporal.nombre)
            temporal = temporal.siguiente    
            
    def recorrercadamatriz(self,pasadas):
        temporal = self.primero
        i = 0
        while temporal is not None:
            if i == pasadas:
                return temporal
            else:
                i += 1    
            temporal = temporal.siguiente

    def eliminartodo(self):
        self.primero = None

    def eliminarnodo(self, nodo):
        temporal = self.primero
        i = 0
        while temporal is not None:
            temporal = temporal.siguiente   


    def mensajexml(self):
        temporal = self.primero
        mensaje = "<Matrices_Resultantes>\n"
        #print("<Matrices_Resultantes>\n")
        #mensaje +="XXXXXXXXXXXXXXXXXXXXXXXXX"
        a = ""
        b = ""
        while temporal is not None:
            #print("NOMBRE:",temporal.nombre, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas)
            #print("-----------------DATOS-------------------")
            mensaje += "    <matriz nombre=\""+str(temporal.nombre)+"\" n=\""+str(temporal.filas)+"\" m=\""+str(temporal.columnas)+"\" g=\""+str(temporal.gruposexistentes)+"\">\n"
            #if(temporal.datos.mensajexml(mensaje) != None):
            a = temporal.datos.mensajexml()
            print("-------------------A-------------------------")
            print(a)
            print("---------------------------------------------")
                #print(temporal.datos.mostrardatos())
                #x = 0
            #if (temporal.grupos.mensajexml(mensaje) != None):
             #   x = 0
            b = temporal.grupos.mensajexml()
                #print(temporal.grupos.mostrardatos())    
            #print("-----------------------------------------")
            #while tmp is not None:
             #   print("X:",tmp.datos.)
            mensaje += a
            mensaje += b
            mensaje += "    </matriz>\n"
            temporal = temporal.siguiente

        mensaje += "</Matrices_Resultantes>\n"
        return mensaje 
            