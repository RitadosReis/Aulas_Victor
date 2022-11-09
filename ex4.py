#5 ate 7 infantil a
#8 ate 10 infantil b
#11 13 juvenil a
#14 17 juvenil b
#18 adulto

def init():
    idade = int(input('Digite sua idade: '))


    if idade < 5:
        print('Voce nao pode participar ainda')
    elif idade >= 5 and idade <= 7:
        print(f'Sua idade é {idade} e vc é do Infantil A')
    elif  idade >= 8 and idade <= 10:
        print(f'Sua idade é {idade} e vc é do Infantil B')
    elif  idade >= 11 and idade <= 13:
        print(f'Sua idade é {idade} e vc é do Juvenil A')
    elif  idade >= 14 and idade <= 17:
        print(f'Sua idade é {idade} e vc é do Juvenil B')
    else:
        print(f'Sua idade é {idade} e vc é do Adulto')