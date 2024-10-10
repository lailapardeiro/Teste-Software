
import random
lista = [random.randint(1, 100) for _ in range(5)]

def main():

    def adicionar_numero(lista, numero):
        lista.append(numero)
        print(f"Número {numero} adicionado à lista.")

    def remover_numero(lista, numero):
        try:
            lista.remove(numero)
            print(f"Número {numero} removido da lista.")
        except ValueError:
            print(f"Número {numero} não existe na lista.")

        def exibir_lista(lista):
            print("Lista atual:", lista)

    




    while True: 
        print('Operações: ')
        print('1. Adicionar um número à lista.')
        print('2. Remover um número da lista.')
        print('3. Exibir a lista atual.')
        print('4. Calcular a soma dos números da lista.')
        print('5. Calcular a média dos números da lista.')
        print('6. Sair do programa.')
        operacao = input('Digite a operação que você deseja realizar: ')


        if opcao == "1":
            numero = int(input("Digite o número a ser adicionado: "))
            adicionar_numero(lista, numero)
        elif opcao == "2":
            numero = int(input("Digite o número a ser removido: "))
            remover_numero(lista, numero)
        elif opcao == "3":
            exibir_lista(lista)




















