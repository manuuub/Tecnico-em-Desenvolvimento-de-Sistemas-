numeros = []
qtd_pares = 0
qtd_impares = 0

for i in range(10):
    num = int (input("Digite um número:"))
    numeros.append(num)

for numero in numeros:
    if(numero*2 == 0):
        qtd_pares = qtd_impares +1

    else:
        qtd_impares = qtd_pares +1

print("O quantidade de pares é:",qtd_pares)
print("O quantidade de impares é:",qtd_impares)