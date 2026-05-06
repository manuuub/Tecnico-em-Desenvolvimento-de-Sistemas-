# codigo ruim
a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a+b+c+d)/ 4

if x >=7:
    print("OK")
elif x >=5:
    print("REC")
else:
    print("NO")

#CLEAN CODE 1
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda  nota:"))
nota3 = float(input("digite a terceira nota:"))
nota4 = float(input("digite a quarta nota:"))
media = (nota1 + nota2 + nota3 + nota4)/4

print("Sua média é:",media)

if(media >= 7):
    print("Aprovado!")
elif(media >= 5):
    print("Recuperação!")
elif(media < 5 ):
    print("Reprovado!")
else:
    print("Dados invalidos!")

#CLEAN CODE 2
notas = []

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ªnota:")))

media = sum(notas)/len(notas)

print("Sua média é:",media)

if(media >= 7):
    print("Aprovado!")
elif(media >= 5):
    print("Recuperação!")
elif(media < 5 ):
    print("Reprovado!")
else:
    print("Dados invalidos!")
