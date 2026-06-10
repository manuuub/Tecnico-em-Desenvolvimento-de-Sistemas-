print("-----Menu de Opcão-----")
print("1 -Econômica")
print("2 - Conforto")
print("3 - Luxo")
opcao = int(input("Digite uma opção:"))

match opcao :
    case 1:
        print("você vai de econômica 🛵")
    case 2:
        print("você vai de conforto 🚗")
    case 3:
        print("você vai de luxo 🚙")
    case _:
        print("❌ Opção Invalida")