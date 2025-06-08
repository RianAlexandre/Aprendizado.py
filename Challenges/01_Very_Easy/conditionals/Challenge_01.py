# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.
from random import randint

userTry = int(input('Enter a integer number from 1-5: '))
numRand = randint(1,5)
if userTry == numRand:
    print(f'You win! The number {numRand} is correct.')
else:
    print(f'You lost, the correct number is {numRand}.')
