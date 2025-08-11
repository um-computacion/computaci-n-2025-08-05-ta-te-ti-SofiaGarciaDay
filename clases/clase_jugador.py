class Jugador:
    def __init__(self, ficha: str, nombre: str):
        self._ficha = ficha
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def getFicha(self):
        return self._ficha
