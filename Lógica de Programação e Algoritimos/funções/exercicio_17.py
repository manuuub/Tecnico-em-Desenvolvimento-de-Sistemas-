numeros = []

for i in range (6):
    numeros.append(int(input("Digite um numero:")))

for i in range (6):
    if(numeros [i]< 0):
        print("Negativo:",numeros [i])
        numeros[i] = 0
    
print(numeros)