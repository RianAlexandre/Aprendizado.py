# FAÇA UM PROGRAMA QUE LEIA UMA FRASE INSERIDA PELO USUÁRIO E MOSTRE:
# 1- QUANTAS VEZES APARECE A LETRA "A"
# 2- EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
# 3- EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

wordInput = str(input("Enter a random phrase: ").upper())
length = len(wordInput)
verify = print(f'A letra "A" aparece {wordInput.count("A")} vezes, pela primeira vez na posição {wordInput.find("A")+1}, e pela última vez na posição {wordInput.rfind("A")+1}')