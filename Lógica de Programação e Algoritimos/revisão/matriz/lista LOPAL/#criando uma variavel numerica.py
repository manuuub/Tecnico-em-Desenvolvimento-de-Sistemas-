#criando uma variavel numerica 
numero = 10

#criando uma variavel textual 
nome = "Gabriel"

#usuario inserir um texto 
nome_completo = input("Digite seu nome:")

#usuario inserir um numero inteiro 
idade = int (input("Digite sua idade :"))

#usuario inserir um numero decimal 
salario = float (input("Digite seu salario:"))

#estruturas condicionais - if
if (salario > 1500 and idade >=18):
    print("Você pode tirar carta !")
elif (salario < 1500 or idade <18 ):
    print("Você não pode tirar carta!")
else:
    print("Invalido")
    #estruturas condicionais 2
turno = input ("Digite seu turno (M/V/N):")

if (turno =="M"):#utilize dois iguais para comparar
    print("Bom dia !")
elif (turno == "V"):
    print ("Boa tarde!")
elif (turno =="N"):
    print("Boa noite!")
else:#else não tem parêntes 
    print ("Invalido")

    #estrutura de repetição 
    #0->10
for i in range (11):#sempre coloque +1
    print (i)

    #1->15
for i in range (1,15):#vai do 1 ate 15 
    print(i)
#5->65(aumentando de 5 em 5)
for i in range (5,66,+5):
    print(i)

#122-> 0 (tirando de 2 em 2 )
for i in range (122,-1 , -2):
    print(i)
#usuario escolhe o ini
#
