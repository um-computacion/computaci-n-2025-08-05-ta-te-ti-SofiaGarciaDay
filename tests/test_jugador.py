import unittest
from clases.clase_jugador import Jugador

class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("O", "Mariana")
    def test_nombre(self):
        self.assertEqual(self.jugador.getNombre(), "Mariana")
    def test_ficha(self):
        self.assertEqual(self.jugador.getFicha(), "O")

if __name__ == '__main__':
    unittest.main()