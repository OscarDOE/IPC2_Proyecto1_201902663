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
    print("2. Desplegar Lista Ordenada")
    print("3. Desplegar Búsquedas")
    print("4. Desplegar Todas")
    print("5. Desplegar Todas a Archivo")
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
    for datos in root:
        #print("NOMBRE: ",datos.attrib['nombre'], "N:", datos.attrib['n'], "M:",datos.attrib['m'])
        Matrices.insertar(datos.attrib['nombre'],datos.attrib['n'],datos.attrib['m'])
        MatrizCode.insertar(datos.attrib['nombre'],datos.attrib['n'],datos.attrib['m'])
        posiciones = ListaDatos()
        posicionesCode = ListaDatos()
        for subdatos in datos:
            posiciones.insertar(subdatos.attrib['x'],subdatos.attrib['y'],subdatos.text,datos.attrib['n'],datos.attrib['m'])
            valor = int(subdatos.text)
            if valor != 0:
                posicionesCode.insertar(subdatos.attrib['x'],subdatos.attrib['y'],1,datos.attrib['n'],datos.attrib['m'])
            else:
                posicionesCode.insertar(subdatos.attrib['x'],subdatos.attrib['y'],0,datos.attrib['n'],datos.attrib['m'])
        
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

def Escribir_Salida():
    print("Opcion 3")

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
    input("Escoja una matriz a graficar")

    with open("1fcdc.dot","w") as f:    
        f.write("digraph grafica{\n")


        f.write("\"Matrices\"[shape=box,style=bold,fillcolor=black, color=orange]\n")
        Matrices.mostrardatos

        
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
    os.system('dot -Tjpg 1fcdc.dot -o graficac1.png')


def Salir():
    print("----------------------------")
    print("Opcion 6")
    print("----------------------------")
    print("Cerrando Programa")
    sys.exit()
menu()
