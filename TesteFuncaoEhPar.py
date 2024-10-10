import unittest 

from funcaoEhPar import eh_par

class TestEhPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(4))

    def test_impar(self):
        self.assertFalse(eh_par(3))

if __name__ == '__main__':
    unittest.main()