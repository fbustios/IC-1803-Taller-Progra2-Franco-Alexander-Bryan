from sys import stdin

def Output(matriz):
    for fila in matriz:
        string = ""
        for char in fila:
            string += char
        print(string)

def matNula(filas, columnas):
    matN = []
    for _ in range(filas):
        filaNula = []
        for _ in range(columnas):
            filaNula.append(".")
        matN.append(filaNula)
    return matN

def isEmpty(stack):
    return len(stack) == 0

def esSol(matriz):
    for fila in matriz:
        if "." in fila: return False
    return True

def rotarMatriz(ficha):  
    lista=[]  
    lista.append(ficha)  
    for _ in range(3):  
        ficha=lista[-1]  
        filas=len(ficha)  
        columnas=len(ficha[0])  
        rotada=[]  
        for i in range(columnas-1,-1,-1):  
            filaNueva=[]  
            for j in range(filas):  
                filaNueva.append(ficha[j][i])  
            rotada.append(filaNueva)  
        lista.append(rotada)  
    return lista

def posiciones(ficha):
    listaPos = []
    for i in range(len(ficha)):
        for j in range(len(ficha[0])):
            if ficha[i][j] != ".":
                listaPos.append((i, j))
    return listaPos

def IzqArribaMax(lista, tupla):
    a, b = tupla
    listaN = []
    for i in lista:
        listaN.append((i[0] - a, i[1] - b))
    return listaN

def Min(ficha):
    pos = posiciones(ficha)
    minimocolumnas = 10<<31
    minimofilas = 10<<31
    for pos in pos:
        if pos[1] < minimocolumnas:
            minimocolumnas = pos[1]
        if pos[0] < minimofilas:
            minimofilas = pos[0]
    return (minimofilas, minimocolumnas)

def Max(lista):
    maximocolumnas = 0
    maximofilas = 0
    for pos in lista:
        if pos[1] > maximocolumnas:
            maximocolumnas = pos[1]
        if pos[0] > maximofilas:
            maximofilas = pos[0]
    return (maximofilas, maximocolumnas)

def caracter(ficha):
    for fila in ficha:
        for char in fila:
            if char != ".":
                return char
    return None

def ponePieza(matriz, lista, icono):
    for i, j in lista:
        matriz[i][j] = icono
    return matriz

def copiarmatriz(matriz):
    matU = matNula(len(matriz), len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matU[i][j] = matriz[i][j]
    return matU

def MueveYValida(matriz, ficha, icono):
    a, b = Min(ficha)
    lista_pos = posiciones(ficha)
    listaN = IzqArribaMax(lista_pos, (a, b))
    n, m = Max(listaN)
    listaMat = []
    for i in range(len(matriz) - n):
        for j in range(len(matriz[0]) - m):
            listaValidos = []
            for x, y in listaN:
                if matriz[x + i][y + j] != ".":
                    break
                listaValidos.append((x + i, y + j))
            if len(listaValidos) == len(listaN):
                matrizU = copiarmatriz(matriz)
                listaMat.append(ponePieza(matrizU, listaValidos, icono))
    return listaMat

def sacarHijos(matriz, piezaausar):
    hijos = []
    pieza = listaPiezas[piezaausar]
    icono = caracter(pieza)
    piezasrotadas = rotarMatriz(pieza)
    for pieza_rotada in piezasrotadas:
        nuevos_hijos = MueveYValida(matriz, pieza_rotada, icono)
        for hijo in nuevos_hijos:
            hijos.append(hijo)
    return hijos

def todo(matriz):
    stack = [(matriz, 0)]
    while not isEmpty(stack):
        estado, piezaquedebousar = stack.pop()
        if esSol(estado): 
            Output(estado)
            return
        if piezaquedebousar < len(listaPiezas):
            hijos = sacarHijos(estado, piezaquedebousar)
            for h in hijos:
                stack.append((h, piezaquedebousar + 1))
    print("No solution")

largo,ancho,piezas=input().split()
listaPiezas=[]
pieza=[]
for linea in stdin:
    if(len(pieza)==4):
        listaPiezas.append(pieza)
        pieza=[]
    fila=list(linea.strip())
    pieza.append(fila)
listaPiezas.append(pieza)
matriz=matNula(int(largo),int(ancho))
todo(matriz)