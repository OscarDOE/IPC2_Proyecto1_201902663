from listadatos import ListaDatos
from listamatrices import ListaMatrices
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
MatrizCode = ListaMatrices()
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
    print("IIIIIIIIIIIIIIIIIIII")
    for i in range(1):
        print(i)
    for datos in root:
        #print("NOMBRE: ",datos.attrib['nombre'], "N:", datos.attrib['n'], "M:",datos.attrib['m'])
        Matrices.insertar(datos.attrib['nombre'],int(datos.attrib['n']),int(datos.attrib['m']))
        MatrizCode.insertar(datos.attrib['nombre'],int(datos.attrib['n']),int(datos.attrib['m']))
        posiciones = ListaDatos()
        posicionesCode = ListaDatos()
        for subdatos in datos:
            posiciones.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),int(subdatos.text),int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
            valor = int(subdatos.text)
            if valor != 0:
                posicionesCode.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),int(subdatos.text),int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
            else:
                posicionesCode.insertar(int(subdatos.attrib['x']),int(subdatos.attrib['y']),int(subdatos.text),int(datos.attrib['n']),int(datos.attrib['m']),datos.attrib['nombre'])
        
        ameter = Matrices.getNodoMatriz(str.lower(datos.attrib['nombre']))
        ametercode = MatrizCode.getNodoMatriz(str.lower(datos.attrib['nombre']))
        #print(ameter)
        ameter.datos = posiciones
        ametercode.datos = posicionesCode
    Matrices.mostrardatos()
    print("-------------CODIFICADA-----------------")
    MatrizCode.mostrardatos()
        #posiciones.mostrardatos()
    #print(root)
    menu()

def Procesar_Datos():
    print("----------------------------")
    print("Opcion 2")
    print("----------------------------")
    print("Procesando Datos")
    print("Transformando las matrices")
    menu()

def Escribir_Salida():
    print("----------------------------")
    print("Opcion 3")
    print("----------------------------")

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
        print("F:",f)
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
        print("TAMAÑO:",tamanio,"COLUMNAS:",columnas)
        print("IIIIIIIIIIIIIIII")
        valor = None
        filas_pasada = 0
        for i in range(filas):
            print("X")
            valorfilas = Grafo.datos.recorrercadan(filas_pasada)
            print("VALORX:",valorfilas) 
            jota = 0
            col = "X"+str(i)
            mensaje += col+"[label=\""+str(valorfilas)+"\"]"+"\n"
            mensaje += str(f)+"->"+col+"\n"
            for j in range(columnas):
                print("Y")
                jota += columnas
                recorrido_columna = Grafo.datos.recorrerm(filas_pasada,jota,Grafo.columnas)
                
                print("VALORY:",recorrido_columna)
                fil = "X"+str(i)+"Y"+str(j)
                
                if recorrido_columna is None:
                    l= 0
                else:    
                    mensaje += fil+"[label=\""+str(recorrido_columna)+"\"]"+"\n"
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













    '''with open("1fcdc.dot","w") as f:    

        mensaje = ""
        mensaje += "digraph grafica{\n"
        mensaje+="\"Matrices\"[shape=box,style=bold,fillcolor=black, color=orange]\n"
        #Matrices.mostrardatos()
        try:
            if x == Matrices.getNodoMatriz(x).nombre:
                print("Se graficará la matriz:",x)
                g = Matrices.getNodoMatriz(x)

            else:    
                print("No ha seleccionado ninguna matriz correctamente")
                menu()
        except:
            print("No ha escrito la matriz correctamente")
            menu()
        
        f.write("\"Nombre Completo\"[shape=box,style=bold, color=red]\n")


        f.write("Carné[shape=box,style=bold, color=red]\n")
        f.write("Curso[shape=box,style=bold, color=red]\n")
        f.write("Sección[shape=box,style=bold, color=red]\n")
        f.write("\"Datos Personales\" -> \"Nombre Completo\", Carné, Curso\n")
        f.write("\"Nombre Completo\" -> \"Oscar Daniel Oliva España\"\n")
        f.write("Carné -> 201902663\n")
        f.write("Curso -> \"Lenguajes Formales\"\n") 
        f.write("\"Lenguajes Formales\" -> Sección\n")
        f.write("Sección -> \"B-\"\n")
        f.write("}\n")
    os.system('dot -Tjpg 1fcdc.dot -o graficac1.png')'''


def Salir():
    print("----------------------------")
    print("Opcion 6")
    print("----------------------------")
    print("Cerrando Programa")
    sys.exit()
menu()
