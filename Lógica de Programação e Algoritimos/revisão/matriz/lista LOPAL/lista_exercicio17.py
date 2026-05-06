palavra = input("Digite uma palavra:")

vogais= "aeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador +=1
print("Quantidade de vogais :",contador )