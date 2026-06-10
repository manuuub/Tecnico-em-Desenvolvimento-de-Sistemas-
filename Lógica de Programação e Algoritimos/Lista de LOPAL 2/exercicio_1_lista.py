bebida = input("Digite o sabor da bebida:")
qtd = int(input("Digite a quantidade desejada :"))
preco = float(input("Digite o preço da bebida:"))

def calcular_total(preco,qtd):
    total = preco*qtd
    print("O valor total é:",total)

calcular_total(preco,qtd)