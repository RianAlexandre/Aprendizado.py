# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
from random import choice

student1 = str(input("Enter first student name: "))
student2 = str(input("Enter second student name: "))
student3 = str(input("Enter third student name: "))
student4 = str(input("Enter fourth student name: "))
allStudents = [student1,student2,student3,student4]

sort = choice(allStudents)

print(f"The student sorted to clean the board is: {sort}")