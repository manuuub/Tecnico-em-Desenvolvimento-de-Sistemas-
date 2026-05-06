saltos = []

for i in range(7):
    saltos.append(int(input("Digite o valor do salto: ")))

# Todos os saltos na ordem em que foram realizados 
print(saltos)

#Maior 
maior = saltos [0]

for salto in saltos:
    if(salto > maior):
        maior = salto

print("O maior salto é:",maior)

#Menor
menor  = saltos [0]

for salto in saltos:
    if(salto < maior):
        menor  = salto

print("O menor salto é:",menor )

#Media sem maior e menor 
soma = 0

for salto in saltos:
    if (salto != maior and salto != menor):
        soma = soma + salto 
media = soma /5 
print("A média sem maior e menor é : ",media )

#Media geral 
soma = 0 

for salto in saltos:
    soma = soma + salto
media_geral = soma /7 
print("A média geral é :",media_geral)