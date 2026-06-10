palavras = []
qtd_mais_que_5 = 0
for i in range (8):
    p = input("Digite uma palavra:")
    palavras.append(p)

for palavra in palavras:
    if(len(palavras)>5):
        print(palavra)
        qtd_mais_que_5+=1

print("Quantidade de palavras com ")