# Para correr los tests: python -m unittest discover -s tests

import unittest
from clases.clase_tateti import Tateti
from clases.clase_jugador import Jugador

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.jugador1 = Jugador("O", "Mariana")
        self.jugador2 = Jugador("X", "Juan")
        self.tateti = Tateti(self.jugador1, self.jugador2)

    def test_parametros_iniciales(self):
        self.assertEqual(self.tateti.getTurno(), "O")
        self.assertEqual(self.tateti.tablero.contenedor, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_ocupar_casilla(self):
        self.assertEqual(self.tateti.getTurno(), "O")
        self.tateti.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(self.tateti.tablero.contenedor[2][2], "O")
        self.assertEqual(self.tateti.getTurno(), "X")
        self.tateti.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.tateti.tablero.contenedor[0][0], "X")

    def test_evaluar_ganador(self):
        self.tateti.ocupar_una_de_las_casillas(2, 0)  
        self.tateti.ocupar_una_de_las_casillas(0, 0)  
        self.tateti.ocupar_una_de_las_casillas(2, 1)  
        self.tateti.ocupar_una_de_las_casillas(1, 1)  
        self.tateti.ocupar_una_de_las_casillas(2, 2)  
        self.assertEqual(self.tateti.evaluar_ganador(), "O")
    
    def test_evaluar_empate(self):
        self.tateti.ocupar_una_de_las_casillas(0, 0)  
        self.tateti.ocupar_una_de_las_casillas(0, 1) 
        self.tateti.ocupar_una_de_las_casillas(0, 2)  
        self.tateti.ocupar_una_de_las_casillas(1, 1)  
        self.tateti.ocupar_una_de_las_casillas(1, 0)  
        self.tateti.ocupar_una_de_las_casillas(1, 2)  
        self.tateti.ocupar_una_de_las_casillas(2, 1)  
        self.tateti.ocupar_una_de_las_casillas(2, 0)  
        self.tateti.ocupar_una_de_las_casillas(2, 2) 
        self.assertIsNone(self.tateti.evaluar_ganador())
        self.assertTrue(self.tateti.evaluar_empate())

if __name__ == '__main__':
    unittest.main()