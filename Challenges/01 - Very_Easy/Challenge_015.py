# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE EM KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O
# CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.-->

kmtraveled = float(input("How many kilometers did you traveled? "))
qtdays = int(input("How many days did you keep the car? "))
print(f"You need to pay a total of ${(kmtraveled * 0.15) + (qtdays * 60)}")