# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m²

# Aqui eu aprendi a usar f-strings

width = float(input("Write the wall width length: "))
height = float(input("Write the wall height length: "))
# print("This wall has a total of {}m² and will require {}L of paint to paint it!".format((width * height),((width * height)/2)))*
print(f"This wall has a total of {(width * height)}m² and will require {((width * height)/2)}L of paint to paint it!")
