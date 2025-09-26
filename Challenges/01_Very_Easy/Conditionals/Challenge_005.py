# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Em geral, um ano é bissexto se for divisível por 4, mas anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.


currentYear = int(input('Enter the current year: '))
if (currentYear % 4 == 0) & (currentYear % 100 == 1) or (currentYear % 400 == 0):
    print('BISSEXTO!!! =)')
else: print('NÃO bissexto!! =(')