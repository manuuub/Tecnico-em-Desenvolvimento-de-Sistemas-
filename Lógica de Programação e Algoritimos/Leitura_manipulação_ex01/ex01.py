# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "Nome":   [],
    "Disciplina":  [],
    "Nota": []
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados:")
    nome = input("Nome: ")
    disciplina = input("Disciplina: ")
    nota = input("Nota: ")

    dados ["Nome"].append(nome)
    dados ["Disciplina"].append(disciplina)
    dados ["Nota"].append(nota)

    deseja_continuar = input("Deseja continuar? (s/n): ").strip().lower()
    #strip()->tirar espaços em branco
    #lower()->transformar em minúsculo
df = pd.DataFrame(dados)
print(df)

#definir o caminho onde será salvo o arquivo
os.chdir("C:\\Users\\45307743840\\Documents\\Leitura_manipulação_ex01\\")

df.to_csv("dados.txt",sep="\t",index=False)
print("Dados salvos em 'dados.txt'!")

#Leitura dos arquivos
try:
    df_lido = pd.read_csv("dados.txt",sep= "\t")

    if(df_lido is not None):
        print("\n dados carregados:")
        print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")