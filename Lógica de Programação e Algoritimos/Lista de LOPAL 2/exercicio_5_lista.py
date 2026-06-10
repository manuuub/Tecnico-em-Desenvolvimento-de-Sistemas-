dados_aluno = {}

dados_aluno["Nome"] = input("Digite o nome :")
dados_aluno["Idioma"] = input("Digite seu idioma:")
dados_aluno["Nivel"] = input("Digite seu nivel:")
dados_aluno["Valor da mensalidade"] = input("Digite o valor da mensalidade:")

print(dados_aluno["Nome"])
print(dados_aluno["Idioma"])
print(dados_aluno["Nivel"])
print(dados_aluno["Valor da mensalidade"])

def mostrar_matricula(dados_aluno):
    mostrar_matricula = dados_aluno