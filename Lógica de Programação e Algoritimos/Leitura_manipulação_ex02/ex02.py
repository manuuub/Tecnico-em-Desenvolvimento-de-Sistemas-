# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "Id":   [],
    "Nome":  [],
    "Quantidade": [],
    "Preco":[]
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados:")
    Id = input("Id: ")
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    preco =float (input("preco: "))

    dados ["Id"].append(Id)
    dados ["Nome"].append(nome)
    dados ["Quantidade"].append(quantidade)
    dados ["Preco"].append(preco)

    deseja_continuar = input("Deseja continuar? (s/n): ").strip().lower()
    #strip()->tirar espaços em branco
    #lower()->transformar em minúsculo
df = pd.DataFrame(dados)
print(df)

#definir o caminho onde será salvo o arquivo
os.chdir("C:\\Users\\45307743840\\Documents\\Leitura_manipulação_ex02\\")

df.to_csv("estoque.cvs",sep="\t",index=False)
print("Dados salvos em 'estoque.cvs'!")

#Leitura dos arquivos
try:
    df_lido = pd.read_csv("estoque.cvs",sep= "\t")

    if(df_lido is not None):
        print("\n dados carregados:")
        print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")
    