# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

fullName = input('Enter your fullname: ').title()
verify = 'Silva' in fullName
print(f"Your fullname's {fullName} so, the return is {verify}")