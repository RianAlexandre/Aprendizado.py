# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

fullName = input('Enter your fullname: ').strip()
verify = 'Silva' in fullName.title()
print(f"Your fullname's {fullName} so, the return is {verify}")


