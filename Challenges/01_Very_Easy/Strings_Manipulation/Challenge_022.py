# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# 1- O NOME COMPLETO COM TODAS AS LETRAS MAIÚSCULAS
# 2- O NOME COM TODAS AS LETRAS MINÚSCULAS
# 3- QUANTAS LETRAS AO TOTAL (SEM CONSIDERAR ESPAÇOS)
# 4- QUANTAS LETRAS TEM O PRIMEIRO NOME

fullName = str(input("Write your full name: ")).strip()
firstNameLetters = fullName.split()
fullNameLetters = fullName.replace(" ","")

print(str(f"Your full name in all capital letters is {fullName.upper()}."))
print(str(f"Your full name in all lowercase letters is {fullName.lower()}."))
print(str(f"Your full name has a total of {len(fullNameLetters)} letters."))
print(str(f"Your first name has a total of {len(firstNameLetters[0])} letters."))


