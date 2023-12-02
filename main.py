from functions.menu import menu_usuario
from functions.criptografia import getpass
from functions.menuAnotacao import menu_anotacao
from Crud.usuario import *
from Crud.anotacao import *

while True:
    menu_usuario()
    op = input("Escolha uma opção: ")

    if op == '1':
        username = input("Digite o nome de usuario:")
        password = getpass()

        if check_existing_user(username):
            print("Nome de usuario ja existe!")
        else:
            cadastrar(username, password)
            print("Cadastrado com sucesso!")

    elif op == '2':
        username = input("Digite o nome de usuario:")
        password = getpass()
        login_result = login(username, password)

        if login_result:
            print("Login bem-sucedido!")
            
            while True:
                menu_anotacao()
                op_anotacao = input("Escolha uma opção: ")

                if op_anotacao == '1':
                    conteudo = input("Digite a anotacao: ")
                    insert_anot(conteudo, login_result[0])
                    print("Anotação inserida com sucesso!")

                elif op_anotacao == '2':
                    anotacoes = listAnot(login_result[0])
                    for anotacao in anotacoes:
                        print(f"Anotação: {anotacao[0]}:  {anotacao[1]}")

                elif op_anotacao == '3':
                    idAnotacao = int(input("Digite qual Anotacao voce quer editar? "))
                    conteudo = input("Digite o novo conteudo: ")
                    update_anot(conteudo, idAnotacao, login_result[0])
                    print("Anotação editada com sucesso!")

                elif op_anotacao == '4':
                    idAnotacao = int(input("Digite qual anotacao voce quer deletar? "))
                    delete_anot(idAnotacao, login_result[0])
                    print("Anotação deletada com sucesso!")

                elif op_anotacao == '5':
                    print("Saindo do menu de anotações...")
                    break

        else:
            print("Falha no login.")

    elif op == '3':
        print("Saindo...")
        break

