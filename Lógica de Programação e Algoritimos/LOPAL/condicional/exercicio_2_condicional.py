idade=int(input("Digite sua idade:"))

if(idade>=0 and idade<=12):
    print("Criança!")

elif(idade>=13 and idade<=17):
    print("Adolecente!")
elif(idade>=18 and idade<=59 ):
    print("Adulto!")

else:
    print("Você é um idoso!")