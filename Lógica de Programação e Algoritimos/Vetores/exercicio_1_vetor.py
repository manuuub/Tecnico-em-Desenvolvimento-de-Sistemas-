numeros = []
cont_pares = 0
 

for i in range (10):
  num = int (input("Digite o numero:"))
  numeros.append(num)

  for numero in numeros:
    if(numero%2 == 0):
      cont_pares= cont_pares+1
print("A quantidade de números pares é:",cont_pares)


