"""
input ("número 1")
print (1)
input ("número 2")
print (2)
input ("número 3")
print (3)
input ("número 4")
print (4)
average <- (número1+número2+número3+número4)/4
print ("A média dos número é ")

"""

"""
#forma 1
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
numero3 = int(input('Numero 3: '))
numero4 = int(input('Numero 4: '))

media = (numero1 + numero2 + numero3 + numero4) / 4


print(f'\nA média é igual : {media}')

"""




def init():
    #forma 2
    total = 0

    for i in range(4):
        nota = int(input(f'Digite {i+1}ª nota: '))
        total += nota

    print(f"A média foi de {total/4}")