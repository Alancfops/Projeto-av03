from functions.menu import menu_usuario
from functions.criptografia import getpass
from functions.menuAnotacao import menu_anotacao
from Crud.usuario import *
from Crud.anotacao import *


while True:
    menu_usuario()
    op = input("Escolha uma opção: ")

    try:
        if op == '1':
            username = input("Digite o nome de usuário:")
            password = getpass()

            try:
                if check_existing_user(username):
                    print("Nome de usuário já existe!")
                else:
                    cadastrar(username, password)
                    print("Cadastrado com sucesso!")

            except Exception as e:
                print(f"Erro ao cadastrar usuário: {e}")

        elif op == '2':
            username = input("Digite o nome de usuário:")
            password = getpass()
            login_result = login(username, password)

            try:
                if login_result:
                    print("Login bem-sucedido!")
                else:
                    print("Nome de usuário ou senha inválidos!")

                    while True:
                        menu_anotacao()
                        op_anotacao = input("Escolha uma opção: ")

                        try:
                            if op_anotacao == '1':
                                conteudo = input("Digite a anotação: ")
                                insert_anot(conteudo, login_result[0])
                                print("Anotação inserida com sucesso!")

                            elif op_anotacao == '2':
                                anotacoes = list_anot(login_result[0])
                                for anotacao in anotacoes:
                                    print(f"Anotação {anotacao[0]}:  {anotacao[1]}")

                            elif op_anotacao == '3':
                                idAnotacao = int(input("Digite qual anotação você quer editar? "))
                                conteudo = input("Digite o novo conteúdo: ")
                                update_anot(conteudo, idAnotacao, login_result[0])
                                print("Anotação editada com sucesso!")

                            elif op_anotacao == '4':
                                idAnotacao = int(input("Digite qual anotação você quer deletar? "))
                                delete_anot(idAnotacao, login_result[0])
                                print("Anotação deletada com sucesso!")

                            elif op_anotacao == '5':
                                print("Saindo do menu de anotações...")
                                break

                            else:
                                print("Opção inválida. Tente novamente.")

                        except Exception as e:
                            print(f"Erro durante operação de anotação: {e}")

            except Exception as e:
                print(f"Erro durante login: {e}")

        elif op == '3':
            print("Saindo...")
            break
        
        elif op =='4':
            historico()

        else:
            print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"Erro durante a execução: {e}")
