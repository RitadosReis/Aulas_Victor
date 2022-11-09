import ex1
import ex2
import ex4
from os import system


while True:
    system('cls')
    print('-'*80)
    print('Menu'.center(80, ' '))
    print('-'*80)
    print('1 - Media')
    print('2 - Calculo de volume')
    print('4 - Natação')
    print('0 - Sair')
    print('-'*80)
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        ex1.init()
        system('pause')
    elif opcao == 2:
        ex2.init()
        system('pause')
    elif opcao == 4:
        ex4.init()
        system('pause')
    elif opcao == 0:
        print('Saindo...........')
        system('pause')
        break