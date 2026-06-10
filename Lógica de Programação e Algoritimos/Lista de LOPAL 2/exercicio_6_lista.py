def gerar_resumo(tipo,valor):
    print("Tipo de Ingresso:",tipo)
    print("Valor do Ingresso:",valor)

nome = input("Digite o seu nome:")
print("----Menu de Ingressos----")
print("1 - Normal")
print("2 - Estudante")
print("3 - Idoso")
opcao = int(input("Digite a opção do ingresso:"))

match opcao:
    case 1:
        gerar_resumo("Normal",30)
    case 2:
        gerar_resumo("Estudante",10)
    case 3:
        gerar_resumo("Idoso",20)
    case _:
        gerar_resumo("Opção Invalida!")