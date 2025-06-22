
from utyls import *

#While True, indica un bucle infinito, en el que solo se saldrá si el usuario introduce las coordenadas válidas.

def pedir_coordenadas():
    while True:
        entrada = input("Introduce fila,col (ej. 2,3): ")
        try:
            fila, col = map(int, entrada.split(","))
            #Verificamos que los números estén entre 0 y 9, para que no se salga del tamaño de la tabla(10x10)
            if 0 <= fila < 10 and 0 <= col < 10:
                return (fila, col)
        except:
            pass
        print("Coordenadas inválidas. Intenta de nuevo.")

def main():
    print("¡Hundir la flota!")

    # Crear tableros
    tablero_usuario = crear_tablero()
    tablero_maquina = crear_tablero()

    # Colocar barcos
    esloras = [2, 2, 2, 3, 3, 4] # Variable en la que definimos el tamaño de los barcos. ( Tres barcos de eslora 2, dos barcos de eslora 3 y un barco de eslora 4)

    print("\nColoca tus barcos:")
    for eslora in esloras: # # Recorre la lista de esloras (longitudes) de los barcos que hay que colocar
        while True: # En bucle, hasta que el jugador coloque el barco.
            print(f"Barco de {eslora} casillas:") #Muestra al jugador el tamaño del barco que debe colocar en ese momento.
            mostrar_tablero(tablero_usuario)#muestra visualmente el tablero del jugador
            entrada = input("Introduce dirección (horizontal o vertical): ").lower() #Le pide al jugador que indique la dirección del barco. Utilizo lower para evitar errores de escritura.
            fila, col = pedir_coordenadas() #valida que esté dentro del tablero (0 a 9).

            if entrada == "horizontal" and col + eslora <= 10: # Si la dirección es horizontal y el barco cabe en la fila sin salirse
                barco = [(fila, col + i) for i in range(eslora)]# Crea una lista con las posiciones del barco en esa fila, moviéndose hacia la derecha
            elif entrada == "vertical" and fila + eslora <= 10:
                barco = [(fila + i, col) for i in range(eslora)]
                # Lo mismo, pero a la izq
            else:
                print("¡El barco se sale del tablero! Intentalo de nuevo.")
                continue

            if esta_libre(barco, tablero_usuario):
                colocar_barco(barco, tablero_usuario)
                break #  # Sale del bucle para pasar al siguiente barco
            else:
                print("¡Casillas ocupadas! Intentalo de nuevo.")

    barcos_maquina = colocar_barcos_aleatorios(tablero_maquina, esloras)#coloca los barcos enemigos (de la máquina) en su propio tablero (tablero_maquina).



    # Empieza el juego por turnos
    turno = 1
    while True:
        print(f"\n--- Turno {turno} ---")

        print("\nTu tablero:")
        mostrar_tablero(tablero_usuario)

        print("\nTablero enemigo:")
        mostrar_tablero(tablero_maquina, ocultar=True)

        # Turno del jugador
        print("\nTu disparo:")
        objetivo = pedir_coordenadas()
        resultado = disparar(objetivo, tablero_maquina)
        print(f"Resultado: {resultado}")

        if todos_hundidos(tablero_maquina):
            print("\n¡Ganaste! Has hundido todos los barcos enemigos.")
            break

        # Turno de la máquina
        objetivo = disparo_aleatorio(tablero_usuario)
        resultado = disparar(objetivo, tablero_usuario)
        print(f"\nLa máquina disparó en {objetivo} → {resultado}")


        if todos_hundidos(tablero_usuario):
            print("\nLa máquina ha hundido todos tus barcos. ¡Perdiste!")
            break

        turno += 1

if __name__ == "__main__":
    main()