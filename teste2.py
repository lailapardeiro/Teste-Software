def valida_senha(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

import unittest
class TestValidaSenha(unittest.TestCase):
    def test_senha_valida(self):
        self.assertTrue(valida_senha('senha123'))

    def test_senha_curta(self):
        self.assertFalse(valida_senha('curta'))

    def test_senha_sem_numero(self):
        self.assertFalse(valida_senha('semnumero'))


if __name__ == '__main__':
    unittest.main() 



















# 
    def calcular_soma(lista):
        soma = sum(lista)
        print(f"Soma dos números da lista: {soma}")

    def calcular_media(lista):
        if lista:
            media = sum(lista) / len(lista)
            print(f"Média dos números da lista: {media:.2f}")
        else:
            print("A lista está vazia, não é possível calcular a média.")




        elif opcao == "4":
            calcular_soma(lista)
        elif opcao == "5":
            calcular_media(lista)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()









    import unittest
from programa import adicionar_numero, remover_numero, calcular_soma, calcular_media

class TestPrograma(unittest.TestCase):

    def test_adicionar_numero(self):
        lista = []
        adicionar_numero(lista, 5)
        self.assertIn(5, lista)

    def test_remover_numero(self):
        lista = [5]
        remover_numero(lista, 5)
        self.assertNotIn(5, lista)
        
    def test_calcular_soma(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(calcular_soma(lista), 15)

    def test_calcular_media(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(calcular_media(lista), 3.0)

if __name__ == "__main__":
    unittest.main()