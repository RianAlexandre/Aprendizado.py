# 14RESOLVIDO <!-- # ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM Cº PARA Fº -->

celsius = float(input("Enter the temperature in Celsius: º"))
fahrenheit = float(input("Enter the temperature in Fahreinheit: º"))

print(f"The conversion from {celsius}ºC to Fahrenheit is a total of {(celsius * 1.8) + 32}Fº .")
print(f"The conversion from {fahrenheit}ºF to Celsius is a total of {(fahrenheit - 32)/1.8}Cº ")