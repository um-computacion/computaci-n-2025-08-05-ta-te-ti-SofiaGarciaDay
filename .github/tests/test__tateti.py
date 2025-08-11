import unittest
from clases.tateti import Tateti
from clases.jugador import Jugador

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
        self.tateti.ocuparCasilla(2, 2)
        self.assertEqual(self.tateti.tablero.contenedor[2][2], "O")
        self.assertEqual(self.tateti.getTurno(), "X")
        self.tateti.ocuparCasilla(0, 0)
        self.assertEqual(self.tateti.tablero.contenedor[0][0], "X")

    def test_evaluar_ganador(self):
        self.tateti.ocuparCasilla(2, 0)  
        self.tateti.ocuparCasilla(0, 0)  
        self.tateti.ocuparCasilla(2, 1)  
        self.tateti.ocuparCasilla(1, 1)  
        self.tateti.ocuparCasilla(2, 2)  
        self.assertEqual(self.tateti.evaluarGanador(), "O")
    
    def test_evaluar_empate(self):
        self.tateti.ocuparCasilla(0, 0)  
        self.tateti.ocuparCasilla(0, 1) 
        self.tateti.ocuparCasilla(0, 2)  
        self.tateti.ocuparCasilla(1, 1)  
        self.tateti.ocuparCasilla(1, 0)  
        self.tateti.ocuparCasilla(1, 2)  
        self.tateti.ocuparCasilla(2, 1)  
        self.tateti.ocuparCasilla(2, 0)  
        self.tateti.ocuparCasilla(2, 2) 
        self.assertIsNone(self.tateti.evaluarGanador())
        self.assertTrue(self.tateti.evaluarEmpate())

if __name__ == '__main__':
    unittest.main()