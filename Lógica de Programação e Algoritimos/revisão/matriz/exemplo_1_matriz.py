matriz = [
    ["laranja","romã","maçã-verde","limão","caqui"],
    ["beringela","batata","pimentão","pimenta","pepino"]
]
print(matriz[0]) #imprime a primeira linha (frutas)
print(matriz[0]) #imprime a segunda linha (legumes)

print(matriz[0][2])#imprime maçã-verde
print(matriz[1][3])#imprime pimenta 

print("Frutas:")
print(matriz [0][0])
print(matriz [0][1])
print(matriz [0][2])
print(matriz [0][3])
print(matriz [0][4])

print("Legumes:")
print(matriz [1][0])
print(matriz [1][1])
print(matriz [1][2])
print(matriz [1][3])
print(matriz [1][4])

print("Matriz complita:")
for i in range(2): #linhas
    for j in range (5): #colunas
        print(matriz[i][j])