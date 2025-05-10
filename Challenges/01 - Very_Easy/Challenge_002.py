# DECLARE QUATRO VARIÁVEIS: UMA DO TIPO INTEIRO, UM DO TIPO REAL, UMA DO TIPO TEXTO E UMA DO TIPO BOOLEANO. IMPRIMA CADA UMA DELAS EM LINHAS SEPARADAS.

num = int(input("Enter an integer: "))
text = str(input("Enter any text: "))
boolean = bool(input("Enter a number, any text, or leave blank: "))

print("The number in integer format is {:.0f}".format(num))
print("The number in float format is {:.2f}".format(num))
print("The entered value is of type {}".format(text))
print("The entered value is of type {}".format(boolean))
