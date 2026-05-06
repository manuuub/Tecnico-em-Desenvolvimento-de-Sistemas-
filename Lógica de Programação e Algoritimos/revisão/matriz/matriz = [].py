matriz = []

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ )
for i in range (4):
    linha =[]
    for j in range(4):
        linha.append(int(input((f"Matriz [{i}][{j}]"))))
    matriz.append(linha)

x = int(input("Digite um número para ser procurado:"))
contador = 0 
for i in range (4):
    for j in range (4):
        if (matriz[i][j]== x ):
            print("X")