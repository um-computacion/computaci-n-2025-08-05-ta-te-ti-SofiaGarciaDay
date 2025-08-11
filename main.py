from clases.clase_jugador import Jugador
from clases.clase_tateti import Tateti
from clases.clase_tablero import posicionOcupadaException

def main():
    print("¡Bienvenidos al Ta-te-ti!")

    nombreO = input("Ingrese el nombre del jugador O: ")
    nombreX = input("Ingrese el nombre del jugador X: ")
    
    jugadorO = Jugador("O", nombreO)
    jugadorX = Jugador("X", nombreX)
    juego = Tateti(jugadorO, jugadorX)

    while True:
        print(f"Turno de {jugadorO.getNombre() if juego.getTurno() == 'O' else jugadorX.getNombre()} ({juego.getTurno()})")
        try:
            fila = int(input("Ingrese fila (1-3): ")) - 1
            columna = int(input("Ingrese columna (1-3): ")) - 1
            if not (0 <= fila <= 2 and 0 <= columna <= 2):
                print("Fila y columna deben estar entre 1 y 3.")
                continue

            juego.ocupar_una_de_las_casillas(fila, columna)

        except ValueError:
            print("Debe ingresar números enteros.")
            continue
        except posicionOcupadaException as e:
            print(e)
            continue

        for fila in juego.tablero.contenedor:
            print(" | ".join(c if c != "" else " " for c in fila))
            print("-" * 9)

        ganador = juego.evaluar_ganador()
        if ganador:
            nombre_ganador = jugadorO.getNombre() if ganador == "O" else jugadorX.getNombre()
            print(f"¡Felicidades {nombre_ganador}! Has ganado.")
            break
        elif juego.evaluar_empate():
            print("¡Empate! No hay más movimientos posibles.")
            break

if __name__ == "__main__":
    main()