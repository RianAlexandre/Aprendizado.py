# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

carVelocity = float(input('Enter the car velocity: '))
if carVelocity > 80:
    print(f'You have been fined by R${(carVelocity - 80) * 7:.2f} ')
else:
    print("Go ahead, you aren't fined")
