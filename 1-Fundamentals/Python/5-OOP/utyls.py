import numpy as np
import random


#Creamos una matriz de 10x10 y la rellenamos con "-", simulando agua.
def crear_tablero(tamaño=10):
    return np.full((tamaño, tamaño), "_")


#Recorremos cada coordenada (fila,columna) del barco y coloamos un "0" en el tablero, simulando la posición del barco.
# barco = [(2,3) , (2,4)]

def colocar_barco(barco, tablero):
    for fila, col in barco:
        tablero[fila, col] = "O"

#Si ambas celdas están vacías ("_"), la función devuelve True. Si al menos una está ocupada (con "O", "X", etc.), devuelve False.
def esta_libre(barco, tablero):
    return all(tablero[fila, col] == "_" for fila, col in barco)


def crear_barco(eslora, tamaño=10):
    orientacion = random.choice(["horizontal", "vertical"]) # Se elige aleatoriamente entre las cadenas "horizontal" y "vertical", para determirar de que manera se coloca el barco
    if orientacion == "horizontal":
        fila = random.randint(0, tamaño - 1) # Se escoje una fila aleatoria del 0 (1) al 9 (10)
        col = random.randint(0, tamaño - eslora)# Se escoje una columna aleatoria en la que empieza en 0 y -escolra, para que no se salga del tablero.
        return [(fila, col + i) for i in range(eslora)]# Generamos una lista, en la que se recorre el tamaño del barco(eslora), por cada fila y columna le sumamos i.
    
# Y si elegimos vertical.
    else:
        fila = random.randint(0, tamaño - eslora) # genera un barco en el que la fila empieza en 0 ,hasta -eslora (para que el barco no se salga del tablero)
        col = random.randint(0, tamaño - 1) #Y columna de 0 hasta -1. (Tamaño del tablero)
        return [(fila + i, col) for i in range(eslora)]

def colocar_barcos_aleatorios(tablero, esloras):
    barcos = [] # Creamos una lista vacía donde guardará las posiciones de todos los barcos que vaya colocando.
    for eslora in esloras:
        colocado = False
        while not colocado:
            barco = crear_barco(eslora) #Creamos variable barco, utilizando la función que generamos antes.
            if esta_libre(barco, tablero):
                colocar_barco(barco, tablero)
                barcos.append(barco)
                colocado = True #Se cambia el estado a True, para salir del bucle y seguir colocando los siguientes barcos.
    return barcos # Devolvemos la lista con todos los barcos colocados

def disparar(casilla, tablero):
    fila, col = casilla
    if tablero[fila, col] == "O":
        tablero[fila, col] = "X"
        #Si la casilla (fila,col), contiene un "0", devuelve una "X" e "imprime" tocado.
        return "Tocado"
    elif tablero[fila, col] == "_":
        tablero[fila, col] = "A"
        #Y si la casilla (fila,col), tiene "_" , devuelve una A, "imprimiendo" agua.
        return "Agua"
    else:
        #Y si ya la casilla ya tenía una X o una A, "imprime" Repetido.
        return "Repetido"

def disparo_aleatorio(tablero):
    tamaño = tablero.shape[0]
    while True:
        fila = random.randint(0, tamaño - 1)
        col = random.randint(0, tamaño - 1)
        if tablero[fila, col] in ["_", "O"]:
            return (fila, col)
        
        #Se comprueba si la casilla aún no ha sido disparada:

def todos_hundidos(tablero):
    return not np.any(tablero == "O")

def mostrar_tablero(tablero, ocultar=False):
    for fila in tablero:
        if ocultar:
            print(" ".join("_" if c == "O" else c for c in fila)) # Si c ("0") , están en fila, lo conviertes en "_", para ocultar la posición del barco.
        else:
            print(" ".join(fila))