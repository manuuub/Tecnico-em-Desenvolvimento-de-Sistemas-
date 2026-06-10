numeros = []
qtd_pares = 0
qtd_impares = 0

for i in range(10):
    num = int (input("Digite um número:"))
    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0:
        print("Par:",numero)
        qtd_pares+=1

    else:
        print("Ímpar:",numero)

print("O quantidade de pares é:",qtd_pares)
print("O quantidade de impares é:",qtd_impares)