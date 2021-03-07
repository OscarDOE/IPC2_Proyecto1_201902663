from listadatos import ListaDatos
from listamatrices import ListaMatrices
from ListaMatrizResultante import ListaMatricesResultantes
from ListaDatosResultante import ListaDatosResultantes
import sys
import os
import xml.etree.ElementTree as ET

#ListaEnlazada = ListaEnlazada()
#ListaEnlazada.insertar(1,1,15)
#ListaEnlazada.insertar(1,2,10)
#ListaEnlazada.insertar(1,3,5)

#ListaEnlazada.mostrarnodos()
#La ruta del archivo de prueba es: 
#C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\x.xml
opcion = 0
tree = None
Matrices = ListaMatrices()
Matrices_modificar = ListaMatrices()
MatrizCode = ListaMatrices()
Resultante = ListaMatricesResultantes()
def menu():
    global opcion
    print("------Menu Principal------")
    print("1. Cargar Archivos")
    print("2. Procesar Datos")
    print("3. Archivo de Salida")
    print("4. Datos del Estudiante")
    print("5. Graficar")
    print("6. Salir")
    opcion = 0
    opcion = int(input("Seleccione una opción\n"))
    try:
        if opcion >=1 and opcion <= 6:
            if opcion == 1:
                Cargar_Archivos()
            elif opcion == 2:
                Procesar_Datos()
            elif opcion == 3:
                Escribir_Salida()
            elif opcion == 4:
                Mostrar_Datos()
            elif opcion == 5:
                Grafica()
            elif opcion == 6:
                Salir()
            else: 
                print("El numero no esta dentro del rango")       
                menu() 
        else:
            print("El numero esta fuera del rango")    
            menu()
    except SyntaxError:
        print("No es un dato válido")
        menu()        


def Cargar_Archivos():
    print("----------------------------")
    print("Opcion 1")
    print("------------------------")
    print("------------------------")
    ruta = input("Ingrese la ruta absoluta del archivo: ")
    tree = ET.parse(ruta)
    root = tree.getroot()
    #Matrices = ListaMatrices()
    posiciones = None
    #MatrizCode = ListaMatrices()
    posicionesCode = None
    c = 0
    #print("IIIIIIIIIIIIIIIIIIII")
    for datos in root:
        #print("NOMBRE: ",datos.attrib['nombre'], "N:", datos.attrib['n'], "M:",datos.attrib['m'])
        Matrices.insertar(datos.attrib['nombre'],int(datos.attrib['n']),int(datos.attrib['m']))
        MatrizCode.insertar(datos.attrib['nombre'],int(datos.attrib['n']),int(datos.attrib['m']))
        Matrices_modificar.insertar(datos.attrib['nombre'],int(datos.attrib['n']),int(datos.attrib['m']))
        posiciones = ListaDatos()
        posicionesCode = ListaDatos()
        for subdatos in datos:
            posiciones.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),int(subdatos.text),int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
            valor = int(subdatos.text)
            if valor != 0:
                posicionesCode.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),1,int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
            else:
                posicionesCode.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),0,int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
        
        ameter = Matrices.getNodoMatriz(str.lower(datos.attrib['nombre']))
        ametercode = MatrizCode.getNodoMatriz(str.lower(datos.attrib['nombre']))
        #print(ameter)
        ameter.datos = posiciones
        ametercode.datos = posicionesCode
    #Matrices.mostrardatos()
    #print("-------------CODIFICADA-----------------")
    #MatrizCode.mostrardatos()
        #posiciones.mostrardatos()
    #print(root)
    menu()

def Procesar_Datos():
    print("----------------------------")
    print("Opcion 2")
    print("----------------------------")
    print("Procesando Datos")
    print("Transformando las matrices")
    #a = Matrices.getNodoMatriz("EJEMPLO")
    #a.datos.eliminarfila(2, 1)
    #a.datos.mostrardatos()
    menu()









def Escribir_Salida():
    print("----------------------------")
    print("Opcion 3")
    print("----------------------------")
    flag = False
    cantidad_Matrices = MatrizCode.getcantidad()
    print("CANTIDAD MATRICES:",cantidad_Matrices)
    for k in range(cantidad_Matrices):
        posicion = 0
        Codigo_actual = MatrizCode.recorrercadamatriz(k)
        #Modificame = Matrices_modificar.recorrercadamatriz(k)
        #k es la matriz en la que va
        prueba = Matrices.recorrercadamatriz(k)
        MRestultante = ListaMatricesResultantes()
        MRestultante.insertar(prueba.nombre+"SALIDA")
        columnas = prueba.columnas 
        filas = prueba.filas
        todosdatos = prueba.datos.gettotal()
        print("NOMBRE MATRIZ:", prueba.nombre+"------------------------")
        #Estas filas son las que se tendran en cuenta para comparar
        #comparando = 0
        fillaa = 1
        # Recorriendo las filas que se van a comparar
        for i in range(filas):
            reparando = 0
            Listitatemporalcomparar = None
            Listitatemporalcomparar = ListaDatos()
            LTemporalC = None
            LTemporalC = ListaDatos()
            #Guardando la fila simple a comparar
            print("FILA:",str(fillaa)+"---------------")
            banderita = False
            for j in range(columnas):
                ingresando = prueba.datos.getNodoFila(fillaa,j+1)
                ingresandoC = Codigo_actual.datos.getNodoFila(fillaa, j+1)
                if ingresandoC.flag == True:
                    banderita = True
                else:
                    if ingresando == None:
                        pass
                    else:
                        LTemporalC.insertar(ingresandoC.x, ingresandoC.y, ingresandoC.valor, ingresandoC.filas, ingresandoC.columnas, ingresandoC.nombrematriz)
                        Listitatemporalcomparar.insertar(ingresando.x, ingresando.y, ingresando.valor, ingresando.filas, ingresando.columnas, ingresando.nombrematriz)
            if banderita == True:
                fillaa += 1
                continue
            else:
                print("LISTITATEMPORALCOMPARAR:")
                Listitatemporalcomparar.mostrardatos()
                fillaa += 1
                f = 0
                # Filas a comparar con la que se quiere comparar
                for j in range(filas):
                    #print("TEMPORAL.PRIMERO:",LTemporalC.primero.x)
                    #print("j+1:",j+1, "j:",j)
                    if LTemporalC.primero.x >= j+1:
                        pass
                    else:
                        # recorre cada columna de la fila
                        ###################################################
                        for l in range(columnas):
                            A = LTemporalC.getNodoFila(LTemporalC.primero.x, l+1)
                            B = Codigo_actual.datos.getNodoFila(j+1, l+1)
                            C = prueba.datos.getNodoFila(j+1,l+1)
                            D = Listitatemporalcomparar.getNodoFila(LTemporalC.primero.x, l+1)
                            print("ACODE:" ,str(A.valor)+" X:",str(A.x)+" Y:",str(A.y)+"VALOR REAL:", str(D.valor))
                            print("BCODE:", str(B.valor)+" X:",str(B.x)+" Y:",str(B.y)+"VALOR REAL:", str(C.valor))

                            if A.valor == B.valor:
                                flag = True
                            else:
                                flag = False
                                break
                        print("FLAG:",flag)

                        if flag == True:
                            for l in range(columnas):
                                A = LTemporalC.getNodoFila(LTemporalC.primero.x, l+1)
                                B = Codigo_actual.datos.getNodoFila(j, l+1)
                                C = prueba.datos.getNodoFila(j+1, l+1)
                                D = Listitatemporalcomparar.getNodoFila(LTemporalC.primero.x, l+1)
                                Codigo_actual.datos.getNodoFila(j+1, l+1).flag = True
                                Listitatemporalcomparar.getNodoFila(LTemporalC.primero.x, l+1).valor += C.valor
                                print("LA SUMA DE LOS 2 NUMEROS ES: ", Listitatemporalcomparar.getNodoFila(LTemporalC.primero.x, l+1).valor, "-----------")
                                #Codigo_actual.datos.eliminarfila(j, l+1)
                                #prueba.datos.eliminarfila(j, l+1)
            #ameter = 

        #prueba.datos.eliminarnodo(desde, hasta)
        #prueba.datos.mostrardatos()
    menu()






















    #Matriz_temporal

def Mostrar_Datos():
    print("----------------------------")
    print("Opcion 4")
    print("----------------------------")
    print("Nombre: Oscar Daniel Oliva España")
    print("Carnet: 201902663")
    print("Curso: Introducción a la Programación y Computación 2, Sección: D ")
    print("Semestre: 4to.")

def Grafica():
    print("----------------------------")
    print("Opcion 5")
    print("----------------------------")
    Matrices.mostrarnombresmatrices()
    x = input("Escriba literalmente el nombre de la matriz que desea graficar: ")
    f = None
    try:    
        f = Matrices.getNodoMatriz(x).nombre
        print("Ya se ha graficado la matriz:",f)
        print("Revise en esta misma carpeta la imágen")
    except:
        print("No se ha ingresado el nombre correctamente")  
        menu()  
    if x == f:
        Grafo = Matrices.getNodoMatriz(x)
        file = open("grafica.dot","w") 
        mensaje = "digraph grafica{\n"
        mensaje += "\"Matrices\"[shape=box,style=bold,fillcolor=black, color=orange]\n"
        mensaje += "\"Matrices\" -> "+str(f)+"\n"
        mensaje += str(f)+"->"+"\"n="+str(Grafo.filas)+"\"\n"
        mensaje += str(f)+"->"+"\"m="+str(Grafo.columnas)+"\"\n"
        tamanio = Grafo.datos.gettotal()
        columnas = Grafo.columnas
        filas = Grafo.filas
        #print("FILAS:", Grafo.filas,"COLUMNAS:",Grafo.columnas)
        #print("TAMAÑO:",tamanio,"COLUMNAS:",columnas)
        #print("IIIIIIIIIIIIIIII")
        valor = None
        filas_pasada = 0
        for i in range(columnas):
            #print("I:", i)
            #print("X")
            valorfilas = Grafo.datos.recorrercadan(filas_pasada)
            valorfilasactual = valorfilas.valor
            #print("VALORX:",valorfilas) 
            jota = 0
            col = "X"+str(i)
            mensaje += col+"[label=\""+str(valorfilasactual)+"\"]"+"\n"
            mensaje += str(f)+"->"+col+"\n"
            for j in range(filas):
                #print("J:",j)
                #print("Y")
                jota += columnas
                recorrido_columna = Grafo.datos.recorrerm(filas_pasada,jota,Grafo.filas)
                if recorrido_columna is None:
                    l=0
                else:
                    valoractual = recorrido_columna.valor
                #print("VALORY:",recorrido_columna)
                fil = "X"+str(i)+"Y"+str(j)
                if recorrido_columna is None:
                    l= 0
                else:    
                    mensaje += fil+"[label=\""+str(valoractual)+"\"]"+"\n"
                    if j == 0:
                        mensaje += col+"->"+fil+"\n"
                    else:
                        fil2 = "X"+str(i)+"Y"+str(j-1)
                        mensaje += fil2+"->"+fil+"\n" 
            filas_pasada += 1   
        mensaje += "}"
        file.write(mensaje)
        file.close()
        os.system('dot -Tjpg grafica.dot -o grafica.png')
        menu()

def Salir():
    print("----------------------------")
    print("Opcion 6")
    print("----------------------------")
    print("Cerrando Programa")
    sys.exit()
menu()
'''# i es la fila principal que compara
        print("NOMBRE:",prueba.nombre+"--------------------------")
        for i in range(filas):
            #Estas filas son las que se recorreran para compararse con la 
            #que se esta comparando
            filas_corriendo = 0
            # j es la fila
            for j in range(filas-1):
                #Este es el dato de la fila en la que esta en cada columna
                va_en_fila = 0
                for l in range(columnas):
                    a = Matriz_codigo_actual.datos.recorrercadan((fila_comparando*columnas)+va_en_fila)
                    a_valor = a.valor
                    b = Matriz_codigo_actual.datos.recorrercadan((filas_corriendo*columnas)+columnas+va_en_fila)

                    b_valor = b.valor
                    xx = prueba.datos.recorrercadan((fila_comparando*columnas)+va_en_fila)
                    xx_valor = xx.valor
                    xxx = prueba.datos.recorrercadan((filas_corriendo*columnas)+columnas+va_en_fila)
                    xxx_valor = xxx.valor

                    if a_valor == b_valor:
                        print("ENCONTRO IGUALACION")
                        print("XX:",xx_valor,"XXX:",xxx_valor)
                        print("A:",a_valor,"B:",b_valor)
                        print("CERRO IGUALACION")
                        flag = True
                    else:
                        print("FLAG == FALSE")
                        print("XX:",xx_valor,"XXX:",xxx_valor)
                        print("A:",a_valor,"B:",b_valor)
                        print("CERRO FALSE")
                        flag = False
                        filas_corriendo += 1
                        break    
                    va_en_fila += 1


                filas_corriendo += 1


            fila_comparando +=1'''