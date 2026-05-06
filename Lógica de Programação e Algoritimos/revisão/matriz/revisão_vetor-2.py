# revisão vetores -1
#solicitar ao usuario a quantidade de numeros  
#preencher o vetor 
#percorrer o vetor e calcular a soma dos números 
#exibir soma
#---------------------------------------

#passo 1) criar as variaveis 
qtd = int (input("Digite a quantidade de números "))
vetor =[]
soma = 0

#passo 2) preencher o vetor
for i in range (qtd):
    vetor.append(int(input("Digite um numero :")))

#passo 3)percorrer o vetor 
for num in vetor :
    soma = soma + num

print("A soma é:",soma)