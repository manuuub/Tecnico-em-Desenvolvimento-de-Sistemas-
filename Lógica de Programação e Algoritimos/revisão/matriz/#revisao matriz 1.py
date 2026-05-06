#revisao matriz 1 
# solicitar a quantidade de linhas 
#solicitar a quantidade de colunas 
#preencher a matriz 
#calcular a soma de todos os numeros 
#---------------------------------------------------------------

#passo 1)variaveis 
linhas = int (input("Digite a quantidade de linhas :"))
colunas = int (input("Digite a quantidade de colunas:"))
matriz = []
soma = 0

#passo 2) preencher matriz 
#sempre repetir quando preencher matriz 
for i in range (linhas):
    linha = []
for j in range (colunas):
    linha.append(int(input("Digite um numero:")))
matriz.append(linha)

#passo 3) percorrer a matriz a calcular a soma 
#sempre repetir quando for percorrer a matriz 
for i in range (linhas):
    for j in range (colunas):
        soma = soma + matriz [i] [j]
print("A soma é:",soma)