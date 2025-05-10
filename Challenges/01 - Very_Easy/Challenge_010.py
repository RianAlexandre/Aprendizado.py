# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR (US$1 = 3.27)


money = float(input("how much money do you have in BRL? "))
print("Converted, your amount of R${:.2f} is equal to ${:.2f}".format(money, money/3.27))