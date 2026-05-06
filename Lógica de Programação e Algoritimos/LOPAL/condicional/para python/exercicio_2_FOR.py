inicio = int(input("digite o numero de inicio:"))
fim = int(input("digite o numero final:"))
soma = 0

for i in range(inicio,fim+1):
    if(i%2 == 0):
        soma = soma + i 

print(soma)