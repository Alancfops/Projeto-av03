from functions.menu import menu_usuario
from functions.criptografia import getpass
from Crud.usuario import *



while True:
    menu_usuario()
    op = input("Escolha uma opção: ")

    if op == '1':
        username = input("Digite o nome de usuario:")
        password = getpass()
        cadastrar( username, password)
        print("Cadastrado com sucesso!")

    elif op == '2':
        username = input("Digite o nome de usuario:")
        password = getpass()
        login_result = login( username, password)
        if login_result:
            print("Login bem-sucedido!")
        else:
            print("Falha no login.")

    elif op == '3':
        print("Saindo...")
        break
    

