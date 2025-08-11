from clases.clase_jugador import Jugador
from clases.clase_tablero import Tablero


class Tateti:
    def __init__(self, jugadorO: Jugador, jugadorX: Jugador):
        self.jugadorO = jugadorO
        self.jugadorX = jugadorX
        self.tablero = Tablero()
        self.turno = "O"

    def getTurno(self):
        return self.turno

    def ocupar_una_de_las_casillas(self, fila: int, columna: int):
        self.tablero.poner_la_ficha(self.turno, fila, columna)
        self.turno = "X" if self.turno == "O" else "O"

    def evaluar_ganador(self):
        t = self.tablero.contenedor
      
        for fila in t:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]
        
        for col in range(3):
            if t[0][col] == t[1][col] == t[2][col] != "":
                return t[0][col]
      
        if t[0][0] == t[1][1] == t[2][2] != "":
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != "":
            return t[0][2]

        return None

    def evaluar_empate(self):
        return self.tablero.getLleno() and self.evaluar_ganador() is None
