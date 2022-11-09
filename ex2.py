#pi r² h
def init():
    pi = 3.1416

    r = int(input('Digite o raio em cm: '))
    h = int(input('Diite a altura em cm: '))


    volume = pi * r**2 * h

    print(f'\nO volume é igual: {volume:.2f}cm³')