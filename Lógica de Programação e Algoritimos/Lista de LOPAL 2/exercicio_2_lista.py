def aplicar_desconto (preco):
    return preco * (1-10/100)

nome_roupa = input("Digite o nome da roupa:")
preco = float(input("Digite o preço da compra:"))

print("Desconto é:",aplicar_desconto(preco))