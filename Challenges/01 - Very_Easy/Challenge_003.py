# LEIA O NOME DE UMA PESSOA COM 4 LETRAS E EXIBA O NOME COM UM HÍFEN ENTRE AS LETRAS, EXEMPLO: JOAO , J-O-A-O

name = str(input("Enter a 4-letter name: "))
print("Your name with a hyphen after each letter will be {}-{}-{}-{}".format(name[0], name[1], name[2], name[3]))
