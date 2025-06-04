# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import hypot

adjacentSide = float(input("Write the length of the adjacent side of the right triangle: "))
oppositeSide = float(input("Write the length of the opposite side of the right triangle: "))
print(f"The Hypotenuse length is {hypot(adjacentSide, oppositeSide):.2f}")