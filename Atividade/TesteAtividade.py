import unittest
from unittest.mock import patch
from atividade import adicionar_numero, remover_numero, calcular_soma, calcular_media

class TestPrograma(unittest.TestCase):
    def setUp(self):
        self.lista = [10, 20, 30]

    def test_adicionar_numero(self):
        adicionar_numero(self.lista, 5)
        self.assertIn(5, self.lista)

    def test_remover_numero(self):
        remover_numero(self.lista, 10)
        self.assertNotIn(10, self.lista) 


    def test_remover_numero_except(self):
        with self.assertRaises(ValueError):
            remover_numero(self.lista, 100)


    def test_calcular_soma(self):
        self.assertEqual(calcular_soma(self.lista), 60)


    def test_calcular_media(self):
        self.assertEqual(calcular_media(self.lista), 20)

if __name__ == "__main__":
    unittest.main()
