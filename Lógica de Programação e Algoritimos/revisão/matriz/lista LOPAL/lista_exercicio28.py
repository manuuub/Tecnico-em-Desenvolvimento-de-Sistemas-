
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o elemento [{i}][{j}]: ")))
    matriz.append(linha)

soma = 0
for i in range(3):
    soma += matriz[i][2 - i] 

print("Soma da diagonal secundária:", soma)
