# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS EX: Nº 1834 , MILHAR: 1, CENTENA: 8, DEZENA: 3, UNIDADE: 4
from random import randint

randNumber = input('Please enter four numbers: ')


thousand = randNumber[0]
hundred = randNumber[1]
ten = randNumber[2]
unit = randNumber[3]
print(f'You choose {randNumber}')
print(f'''The value of thousand is {thousand}\n 
The value of hundred is {hundred}\n
The value of ten is {ten}\n
The value of unit is {unit}''')