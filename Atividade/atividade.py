
import random
lista = [random.randint(1, 100) for _ in range(5)]

def main():

    def adicionar_na_lista(lista):
        adicionar_na_lista = int(input('Digite o número inteiro que você deseja adicionar na lista: '))
        lista.append(adicionar_na_lista)

    def remover_da_lista(lista):
            try:
                remover_da_lista = int(input('Digite o número inteiro que você deseja remover da lista: '))
                lista.remove(remover_da_lista)
            except ValueError:
                print('O número digitado não existe na lista!')

    def exibir_lista(lista):
        print(lista)
    
    def calcular_soma(lista):
        soma = 0
        for numero in lista:
            soma += numero
            return soma




    while True: 
        print('Operações: ')
        print('1. Adicionar um número à lista.')
        print('2. Remover um número da lista.')
        print('3. Exibir a lista atual.')
        print('4. Calcular a soma dos números da lista.')
        print('5. Calcular a média dos números da lista.')
        print('6. Sair do programa.')
        operacao = input('Digite a operação que você deseja realizar: ')


        if operacao == 1:
            def adicionar_na_lista(lista)
        elif operacao == 2:
            def remover_da_lista(lista)
                
            break




