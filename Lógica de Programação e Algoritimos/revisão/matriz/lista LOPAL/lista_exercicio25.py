matriz = [[0, 0, 0], [0, 0, 0]]

for i in range(2): 
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i},{j}]: "))

print("\nMatriz 2x3:")
for linha in matriz:
    print(linha)

print("\nSoma de cada coluna:")
for j in range(3):
    soma_coluna = 0
    for i in range(2):
        soma_coluna += matriz[i][j]
    print(f"Coluna {j}: {soma_coluna}")
