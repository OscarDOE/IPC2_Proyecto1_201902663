from datosresultante import posicion

class ListaDatosResultantes:
    def __init__(self):
        self.primero = None

    def insertar(self,x, y, valor, nombrematriz, columnas):
        nuevo = posicion(x,y,valor, nombrematriz, columnas)
        if self.primero is None:
            self.primero = nuevo
        else: 
            temporal = self.primero    
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo    
            nuevo.anterior = temporal


    #def insertarvarios(self):


    
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

    #def recorrer (self, hasta):
   #     temporal = self.primero
   #     i = 0
    #    while i <= hasta:
     #       if i == hasta:
      #          return temporal
       #     temporal = temporal.siguiente

#Se utilizó para las gráficas, recorría cada espacio de la primera fila
    def recorrercadan(self,pasadas):
        temporal = self.primero
        c = 0
        while temporal is not None:
            if c == pasadas:
                return temporal
            else:
                c += 1
            temporal = temporal.siguiente    
#C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\x.xml
#C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\y.xml

#Se utilizó para las gráficas, recorre cada uno de las columnas, que esta 
#debajo de la función de arriba 
    def recorrerm (self,columna_va, filas_va,columnas):
        temporal = self.primero
        c = 0
        count = 0
        while temporal is not None:
            if count != columna_va:
                temporal = temporal.siguiente
                count += 1
            if filas_va == c:
                return temporal
            else:
                c += 1
            if temporal is None:
                #temporal = temporal.siguiente   
                break
            else:
                temporal = temporal.siguiente

    def eliminartodo(self):
        self.primero = None

    def eliminar_nodo_desde_hasta(self,desde,hasta):
        temporal = self.primero
        i = 0
        j = 0
        #print("DESDE:",desde)
        #print("HASTA:",hasta)
        while temporal is not None:
            if i < desde:
                i += 1
                #print("ANTES DE:", temporal.valor)
                temporal = temporal.siguiente
                #print("DESPUES DE:", temporal.valor)
                #print("I:",i)
            elif i >= desde and i < hasta:
                #print("ESTA ELIMINANDO?")
                eliminando = temporal
                if temporal.siguiente == None:
                    #print("YA")
                    temporal = None
                    break
                else:
                    #print("NEL, I:", i)
                    #print("VALOR:", temporal.valor)
                    temporal = eliminando.siguiente
                    temporal.anterior = eliminando.anterior
                    anterior = eliminando.anterior
                    anterior.siguiente = temporal
                   # temporal = eliminando.anterior    
                   # temporal.siguiente = eliminando.siguiente
                   # siguiente = eliminando.siguiente
                   # siguiente.anterior = temporal
                    eliminando.siguiente = None
                    eliminando.anterior = None
                    i += 1
            else:
                break

    def mensajexml(self):
        print("-------------------------DATOS------------------------")
        temporal = self.primero
        #m = mensaje
        a = ""
        while temporal is not None:
            #print("LLEGO A DATOS")
            #print("X:",temporal.x, "Y:", temporal.y, "VALOR:",temporal.valor, "FILAS:", temporal.filas, "COLUMNAS:",temporal.columnas)
            a += "        <dato x=\""+str(temporal.x)+"\" y=\""+str(temporal.y)+"\">"+str(temporal.valor)+"</dato>\n"
            #print("-----------------------MENSAJE-----------------------")
            #print("-----------------------CIERRA MENSAJE-----------------------")
            temporal = temporal.siguiente
           
        return a
