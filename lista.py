import os


class Lista:
    point = -1
    vetor = [None] * 10


def main():
    condicional = True

    while condicional:
        n = menu()

        if n == 1:  # visualizar
            imprimir()
        elif n == 2:  # adicionar
            inserir()
        elif n == 3:  # remover
            remover()
        elif n == 4:
            condicional = sair()


def menu():
    os.system('clear')

    print('{} \n\n'.format('-=-' * 14))

    print('  \033[36m=== SISTEMA DE LISTAS BASICO ===\033[0m\n')
    print('   Sistema basico de explificacao de\n'
          '  listas. Por favor, tente realizar\n'
          '  alguma acao digitando a opcao abaixo\n\n'
          '  [1]- Visualizar lista\n'
          '  [2]- Adicionar da lista\n'
          '  [3]- Remover da lista\n'
          '  [4]- Sair do programa :D\n\n')

    select = int(input('  ./Selecione: '))

    return select


def inserir():
    os.system('clear')

    print('{} \n\n'.format('-=-' * 14))

    print('  \033[36m=== ADICIONAR UM ITEM A LISTA ===\033[m\n')
    number = int(input('  ./Digite um numero: '))

    Lista.point = Lista.point + 1
    Lista.vetor[Lista.point] = number

    print('\n  Item Adicionado com sucesso :D')
    input('\n\n    \033[31mPressione Enter\033[0m')


def remover():
    os.system('clear')

    print('{} \n\n'.format('-=-' * 14))

    print('  \033[36m=== REMOVER UM ITEM A PILHA ===\033[m\n')
    n = int(input('\n\n  Deseja realmente remover um item da lista\n'
                  '  (1=sim) ? '))

    if n == 1:
        for n in range(9):
            Lista.vetor[n] = Lista.vetor[n+1]

        Lista.point = Lista.point-1
        print('\n\n  Removido com sucesso :D')
    else:
        print('\n\n  Tudo bem, voce quem manda :D')

    input('\n\n    \033[31mPressione Enter\033[0m')


def imprimir():
    os.system('clear')

    print('{} \n\n'.format('-=-' * 14))

    print('  Ponteiro: {}'.format(Lista.point))

    print('\n  Vetor: ', end='')
    for n in Lista.vetor:
        if n is None:
            print('[-]', end='')
        else:
            print('[{}]'.format(n), end='')

    input('\n\n    \033[31mPressione Enter\033[0m')


def sair():
    os.system('clear')

    print('{} \n\n'.format('-=-' * 14))

    print('  \033[36m=== Obrigado por utilizar o sistema ===\033[0m\n'
          '  \033[35m=== By. Danilo A. Silva ===\033[0m')

    print('\n\n{}'.format('-=-' * 14))

    return False


main()

# for n in range(3):
#     vetor[n] = 1
#
# for n in range(10):
#     if vetor[n] is not None:
#         print(vetor[n])
