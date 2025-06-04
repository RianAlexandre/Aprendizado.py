# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA "SANTO"

cityName = input('Digite o nome da cidade: ').title().split()
verify = 'Santo' in cityName[0]
print(f'The first name is {cityName[0]} so, the result return {verify}')