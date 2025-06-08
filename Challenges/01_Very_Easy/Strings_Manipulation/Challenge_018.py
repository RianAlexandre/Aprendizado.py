# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.

from math import sin, cos, tan, radians

angle = radians(float(input("Enter a floating point value as the angle to be calculated: ")))
print(f"""
The sine value of the angle you've entered is {sin(angle):.4f}\n
The cosine value of the angle you've entered is {cos(angle):.4f}\n
The tangent value of the angle you've entered is {tan(angle):.4f}""")