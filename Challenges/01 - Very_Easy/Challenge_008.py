# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metro = float(input("Enter the value in meters: "))
print("The entered value converted to centimeters is {}cm, and converted to millimeters is {}mm".format(metro*100, metro*1000))
