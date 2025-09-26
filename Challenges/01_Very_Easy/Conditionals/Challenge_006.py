# # Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Write a first integer number: '))
num2 = int(input('Write a second integer number: '))
num3 = int(input('Write a third integer number: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior número')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior número')
else:
    print(f'{num3} é o maior número')


# CÓDIGO MAIS EFICIENTE:
# num1 = int(input('Write a first integer number: '))
# num2 = int(input('Write a second integer number: '))
# num3 = int(input('Write a third integer number: '))
#
# maior = max(num1,num2,num3)
#
# print(f'{maior} é o maior número')