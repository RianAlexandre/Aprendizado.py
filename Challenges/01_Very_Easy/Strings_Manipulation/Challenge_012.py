# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO

price = float(input("Enter the current price of the product: $"))
percent = float(input("Enter how much percent % you want to discount: "))
print(f"The price of the product with a {percent:.1f}% discount is ${price - (price/100)*percent:.2f}")