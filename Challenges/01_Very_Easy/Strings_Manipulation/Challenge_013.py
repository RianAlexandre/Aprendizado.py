# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO

salary = int(input("Enter your current salary: $"))
percent = float(input("Enter how much percentage % you want give as bonus: "))
print(f"Your new salary with a bonus of {percent:.1f}% is ${salary + (salary/100)* percent:.2f}")
