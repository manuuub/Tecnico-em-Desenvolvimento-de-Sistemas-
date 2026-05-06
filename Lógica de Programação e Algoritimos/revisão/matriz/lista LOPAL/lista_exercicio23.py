
matriz = [[0, 0], [0, 0]]
soma = 0


print("Digite os elementos da matriz 2x2:")
for i in range(2):
    for j in range(2):
        matriz[i][j] = float(input(f"Elemento [{i}][{j}]: "))


for i in range(2):
    for j in range(2):
        soma += matriz[i][j]


print("-" * 20)
print(f"Matriz: {matriz}")
print(f"A soma de todos os elementos é: {soma}")
print("-" * 20)
