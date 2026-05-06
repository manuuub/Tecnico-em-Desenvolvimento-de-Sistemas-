numeros_pares = []

for i in range(1, 7):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        numeros_pares.append(num)

print("Os números pares é:", numeros_pares)
