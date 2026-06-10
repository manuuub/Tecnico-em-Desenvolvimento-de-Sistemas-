nomes = []
for i in range (6):
    nomes.append(input("Digite um nome:"))
nome_buscar = input("Digite um nome para buscar:")

for nome in nomes:
    if(nome == nome_buscar):
        print("Encontrou!")