class posicion:
    def __init__(self, x, y, valor, filas, columnas, nombrematriz):
        self.x = x
        self.y = y
        self.valor = valor
        self.filas = filas
        self.columnas = columnas
        self.nombrematriz = nombrematriz
        self.siguiente = None
        self.anterior = None
        self.flag = False
        self.frecuencia = 0
        #C:\Users\elmco\OneDrive\Documentos\GitHub\IPC2_Proyecto1_201902663\x.xml