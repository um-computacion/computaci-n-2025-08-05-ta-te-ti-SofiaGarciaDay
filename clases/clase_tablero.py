class posicionOcupadaException(Exception):
    pass


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        self._lleno = False

    def poner_la_ficha(self, ficha: str, fila: int, columna: int):
        if self.contenedor[fila][columna] == "":
            self.contenedor[fila][columna] = ficha
            self._lleno = all(
                casilla != "" for fila_tablero in self.contenedor for casilla in fila_tablero
            )
        else:
            raise posicionOcupadaException("Posición ocupada!")

    def getLleno(self):
        return self._lleno
