numeros= []
media=0 
soma =0

for i in range (6):
    num = int(input("Digite o numero:"))
    numeros.append(num)

    for numero in numeros:
        soma = numero + soma
        media = soma/ 6
print("A média é:", media)
