
numeros = []
soma = 0

for i in range(7):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)

print(f"Vetor: {numeros}")
print(f"Soma dos elementos: {soma}")
