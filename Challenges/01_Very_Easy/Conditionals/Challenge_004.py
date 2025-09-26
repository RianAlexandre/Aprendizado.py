# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

travelDistance = float(input('Enter the travel distance in Kilometers: '))
if travelDistance < 201:
    print(f'The price of your ticket is R${travelDistance * 0.5}.')
else: print(f'The price of your ticket is R${travelDistance * 0.45}.')