# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "Id":   [],
    "Descricao":  [],
    "Status": []
}

deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados:")
    Id = input("Id: ")
    descricao = input("Descrição: ")
    status = input("Status: ")

    dados ["Id"].append(Id)
    dados ["Descricao"].append(descricao)
    dados ["Status"].append(status)

    deseja_continuar = input("Deseja continuar? (s/n): ").strip().lower()
    #strip()->tirar espaços em branco
    #lower()->transformar em minúsculo
df = pd.DataFrame(dados)
print(df)

#definir o caminho onde será salvo o arquivo
os.chdir("C:\\Users\\45307743840\\Documents\\Leitura_manipulação_ex03\\")

df.to_json("tarefas.json",orient="records",indent=False)
print("Dados salvos em 'tarefas.json'!")

#try ->tentar executar esse bloco
try:
    df_lido = pd.read_json("tarefas.json")

    if(df_lido is not None):
        print("\n dados carregados:")
        print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")