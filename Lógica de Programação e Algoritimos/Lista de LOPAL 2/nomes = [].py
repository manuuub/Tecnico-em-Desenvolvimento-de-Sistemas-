nomes = []
opcao =""

while opcao != "fim":
    nomes.append(input("Digite um nome:"))
    opcao = input("Digite fim para sair ou enter para continuar")

print("Quantidade de nomes:",len(nomes))

for nome in nomes:
    print(nome)