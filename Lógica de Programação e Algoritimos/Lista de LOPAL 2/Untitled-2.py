print("-----Menu de Opcão-----")
print("1 - Sem garantia")
print("2 - Garantia de 1 ano")
print("3 - Garantia de 2 anos")
opcao = int(input("Digite uma opção:"))

match opcao :
    case 1:
        print("")
    case 2:
        print("você vai de conforto 🚗")
    case 3:
        print("você vai de luxo 🚙")
    case _:
        print("❌ Opção Invalida")