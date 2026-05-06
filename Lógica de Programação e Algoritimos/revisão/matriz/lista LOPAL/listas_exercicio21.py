soma_pares = 0


for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número: "))
    
    if numero % 2 == 0:                
        soma_pares += numero

print(f"\nA soma dos números pares é: {soma_pares}")
