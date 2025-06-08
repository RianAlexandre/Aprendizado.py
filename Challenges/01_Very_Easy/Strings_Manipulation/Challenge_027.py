# FAÇA UM PROGRAMA QUE LEIA UMA FRASE INSERIDA PELO USUÁRIO E MOSTRE:
# 1- QUANTAS VEZES APARECE A LETRA "A"
# 2- EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
# 3- EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

wordInput = str(input("Enter a random phrase: ").upper())
length = len(wordInput)
verify = print(f'The letter "A" appears {wordInput.count("A")} times, the first time in position {wordInput.find("A")+1}, and the last time in position {wordInput.rfind("A")+1}')