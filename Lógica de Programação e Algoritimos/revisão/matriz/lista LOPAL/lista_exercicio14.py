positivos = 0
negativos = 0

for i in range (10):
    numero = float(input("Digite um numero:"))

if numero > 0 :
    positivos +=1

elif numero <0:
    negativos +=1

print("Quantidade de positivo:",positivos)
print("Quantidade de negativo",negativos)