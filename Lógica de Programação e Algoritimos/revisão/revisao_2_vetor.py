# Solicita um texto para o usuario
texto = input("Digite um texto qualquer:")

#Exibir letra por letra do texto
#Para cada letra no texto
for letra in texto:
    print(letra )

#Contar quantidade de caracteres !=''
qtd_caracteres = 0 

for letra in texto:
    if (letra != " "):
        qtd_caracteres+=1
print("A quantidade de caracteres é :",qtd_caracteres)

# Contar as quantidades de vogais 
vogais = "aeiouAEIOUáàãâÁÀÃÂéèêÉÈÊÊíìîÍÌÎóòôõÓÒÔÕúùûÚÙÛ"
qtd_vogais  = 0 

for vogal in vogais:
    for letra in texto:
        if (letra == vogal):
         qtd_vogais+=1
print("A quantidade de vogais é:",qtd_vogais)

#Palindromo
texto_invertido = ""

for i in range (len(texto)-1,-1,-1):
    texto_invertido = texto_invertido + texto [i]

if(texto == texto_invertido):
    print("É palíndromo!")
else:
    print("Não é palíndromo")