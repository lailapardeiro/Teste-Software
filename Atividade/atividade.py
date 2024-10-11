
import random
lista = [random.randint(1, 100) for _ in range(5)]

def adicionar_numero(lista, numero):
    lista.append(numero)
    print(f"Número {numero} adicionado à lista.")

def remover_numero(lista, numero):
        lista.remove(numero)
        print(f"Número {numero} removido da lista.")


def exibir_lista(lista):
    print("Lista atual:", lista)

def calcular_soma(lista):
    return sum(lista)


def calcular_media(lista):
    if lista:
        return sum(lista) / len(lista)
    else:
        print("A lista está vazia, não foi possível calcular a média.")


def main():
    while True: 
        print('Operações: ')
        print('1. Adicionar um número à lista.')
        print('2. Remover um número da lista.')
        print('3. Exibir a lista atual.')
        print('4. Calcular a soma dos números da lista.')
        print('5. Calcular a média dos números da lista.')
        print('6. Sair do programa.')
        operacao = input('Digite a operação que você deseja realizar: ')


        if operacao == "1":
            numero = int(input("Digite o número a ser adicionado: "))
            adicionar_numero(lista, numero)
        elif operacao == "2":
            try:
                numero = int(input("Digite o número a ser removido: "))
                remover_numero(lista, numero)
            except ValueError:
                print(f"Número {numero} não existe na lista.")


        elif operacao == "3":
            exibir_lista(lista)
        elif operacao == "4":
            soma = calcular_soma(lista)
            print(f"Soma dos números da lista: {soma}")

        elif operacao == "5":
            media = calcular_media(lista)
            print(f"Média dos números da lista: {media:.2f}")
        elif operacao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Operação inválida. Tente novamente!")

if __name__ == "__main__":
    main()
