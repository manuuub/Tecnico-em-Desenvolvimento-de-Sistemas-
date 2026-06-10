matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um valor:")))
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i in range(3):
    for j in range(3):
        if(i == j):
            print(matriz[i][j])