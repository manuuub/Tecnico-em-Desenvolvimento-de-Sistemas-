# Sistema de cadastro de usuarios e produtos
# O sistema deverá permitir:
# - cadastrar
# - listar 
# - deletar

#Criação das listas 
usuarios = []
produtos = []

# ------------------------------------------------------
#------Função Menu Usuarios-------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario !=4):
        print()
        print("------Menu Usuarios------")
        print("1 - Cadastrar Usuario")
        print("2 - Listar Usuario")
        print("3 - Deletar Usuario")
        print("4 - Voltar")
        
        opcao_menu_usuario = int(input("Escolha uma opção: "))

        match opcao_menu_usuario:
            #Cadastrar Usuario
            case 1 :
                nome = input("Digite o nome:")
                telefone = input("Digite o telefone :")
                email = input("Digite o email:")

                #Criação do json de usuarios (chave: valor)
                usuario ={
                    "nome":nome,
                    "telefone":telefone,
                    "email":email
                }

                # Adicionar o jeson no array
                usuarios.append(usuario)
                print(f"Usuario{usuario['nome']}cadastrado com sucesso!")
            #Listar Usuarios
            case 2:
                print("\n Lista de usuários: ")

                if (len (usuarios) == 0):
                    print("Nenhum usuário cadastrado!")
                else:
                    for usu in usuarios :
                        print("---------")
                        print("Nome:",usu["nome"])
                        print("Telefone:",usu ["telefone"])
                        print("Email:",usu["email"])
           #Deletar usuário
            case 3:
             nome_deletar = input("Digite o nome que deseja deletar:")
             encontrado = False

             for usu in usuarios:
                 if(usu ["nome"] == nome_deletar):
                     usuarios.remove(usu)
                     encontrado =True
                     print("Usuário removido com sucesso!")

             if (encontrado == False):
                 print("Usuario não encontrado") 
            #Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break
#----------------------------------------------------------------------------------------------------------------------------
#------Função Menu Produtos-------
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto !=5):
        print()
        print("------Menu Produtos------")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produto")
        print("3 - Deletar Produro")
        print("4 - Calcular Total")
        print("5 - Voltar")
        
        opcao_menu_produto = int(input("Escolha uma opção: "))

        match opcao_menu_produto:
            #Cadastrar Produto
            case 1 :
                nome = input("Digite o nome:")
                descricao = input("Digite a descrição :")
                quantidade = int (input("Digite  a quantidade :"))
                valor = float(input("Digite o valor:"))

                #Criação do json de usuarios (chave: valor)
                produto ={
                    "nome":nome,
                    "descricao":descricao,
                    "valor":valor 
                }

                # Adicionar o jeson no array
                produtos.append(produto)
                print(f"Produto{produto['nome']}cadastrado com sucesso!")
            #Listar Produtos 
            case 2:
                print("\n Lista de Produtos: ")

                if (len (produtos) == 0):
                    print("Nenhum produto cadastrado!")
                else:
                    for pro in produtos :
                        print("---------")
                        print("Nome:",pro["nome"])
                        print("Descrição:",pro ["descricao"])
                        print("Quantidade:",pro["quantidade"])
                        print("Valor:",pro["valor"])
           #Deletar Produto
            case 3:
             nome_deletar = input("Digite o nome que deseja deletar:")
             encontrado = False

             for pro in produtos:
                 if(pro ["nome"] == nome_deletar):
                     produtos.remove(pro)
                     encontrado =True
                     print("Produto removido com sucesso!")

             if (encontrado == False):
                 print("Produto não encontrado") 
            #Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break
#-------------------------------------------------------
#--------Menu Principal--------
opcao_menu = 0
while(opcao_menu != 3):
    print("---Menu - Sistema de Cadastro---")
    print("Opções: ")
    print("1- Usuários")
    print("2- Produtos ")
    print("3- sair")
    opcao_menu = int(input("Escolha uma opção:"))

    match opcao_menu:
        #Menu Principal
        case 1:
            menu_usuarios()
        #Menu Produtos
        case 2:
            menu_produtos()
        case 3:
            print("👋🏼Ate logo!")
        case _:
            print("Opção Invalida!")
