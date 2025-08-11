import unittest
from clases.tablero import Tablero, posicionOcupadaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_get_vacio(self):
        
        self.assertFalse(self.tablero.getLleno())

    def test_poner_ficha(self):
       
        self.tablero.ponerFicha("O", 2, 2)  
        self.tablero.ponerFicha("X", 1, 1)  
        self.assertEqual(self.tablero.contenedor[2][2], "O")
        self.assertEqual(self.tablero.contenedor[1][1], "X")
        self.assertEqual(self.tablero.contenedor[0][0], "")
        self.assertEqual(self.tablero.contenedor[0][1], "")
        self.assertEqual(self.tablero.contenedor[0][2], "")
        self.assertEqual(self.tablero.contenedor[1][0], "")
        self.assertEqual(self.tablero.contenedor[1][2], "")
        self.assertEqual(self.tablero.contenedor[2][0], "")
        self.assertEqual(self.tablero.contenedor[2][1], "")

    def test_poner_ficha_en_posicion_ocupada(self):
        self.tablero.ponerFicha("O", 2, 2)
        with self.assertRaises(posicionOcupadaException):
            self.tablero.ponerFicha("X", 2, 2)

    def test_tablero_lleno(self):
        
        movimientos = [
            ("X", 0, 0), ("O", 0, 1), ("X", 0, 2),
            ("O", 1, 0), ("X", 1, 1), ("O", 1, 2),
            ("O", 2, 0), ("X", 2, 1), ("O", 2, 2)
        ]
        for ficha, fila, col in movimientos:
            self.tablero.ponerFicha(ficha, fila, col)
        self.assertTrue(self.tablero.getLleno())

if __name__ == '__main__':
    unittest.main()