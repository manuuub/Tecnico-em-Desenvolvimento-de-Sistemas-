matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input("Digite um valor:")))
    matriz.append(linha)

for linha in matriz:
    print(linha)