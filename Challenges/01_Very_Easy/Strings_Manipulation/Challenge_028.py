# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE. EX: ANA MARIA DE SOUZA , PRIMEIRO NOME: ANA , ÚLTIMO NOME: SOUZA


fullName = input('Enter your fullname: ').strip().title()
nameSplit = fullName.split() # divide a variável em listas ex: [Ana],[Maria],[Clara] enumerando como lista[0],[1],[2]
print(len(nameSplit)) # Percorre a lista retornando o seu tamanho total, retornará 3 no exemplo acima.
print(f'Your first name is {nameSplit[0]} and your last name is {nameSplit[len(nameSplit)-1]}.') # Pega o len da lista que é (3) e mostra seus índices que são: [0]Ana, [01]Maria, [02]Clara,
# como o len é 3, é necessário adicionar o -1 para que o tamanho da lista não seja ultrapassado.