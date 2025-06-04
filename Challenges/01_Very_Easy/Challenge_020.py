# UM PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
from random import shuffle
aluno1 = input("Enter the first student name: ")
aluno2 = input("Enter the second student name: ")
aluno3 = input("Enter the third student name: ")
aluno4 = input("Enter the fourth student name: ")
sortList = [aluno1, aluno2, aluno3, aluno4]
shuffle(sortList)
print(f"The students presentation order is: {sortList}")