# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA "SANTO"

cityName = input('Enter the city name: ').title().split()
verify = 'Santo' in cityName[0].strip()
print(f'The first name is {cityName[0]} so, the result return {verify}')


# Option 2:
#cityName = input('Enter the city name: ').strip()
#rint(f'The first name is {cityName.split()[0].upper()} so, the result return {cityName[:5].upper() == "SANTO"}')