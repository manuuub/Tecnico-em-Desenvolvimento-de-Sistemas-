notas = []

for i in range(5):
    notas.append(float(input(f"Digite a {i+1}ªnota:")))

soma = sum(notas)

print("Sua soma é:",soma)
