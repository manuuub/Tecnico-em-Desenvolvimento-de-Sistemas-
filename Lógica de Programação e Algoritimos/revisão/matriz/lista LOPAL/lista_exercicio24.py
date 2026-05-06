
matriz = []


print("Digite os elementos da matriz 3x2:")
for i in range(3):
    linha = []
    for j in range(2):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nNúmeros maiores que 10 encontrados:")
encontrou = False
for i in range(3):
    for j in range(2):
        if matriz[i][j] > 10:
            print(matriz[i][j])
            encontrou = True

if not encontrou:
    print("Nenhum número maior que 10 foi encontrado.")
