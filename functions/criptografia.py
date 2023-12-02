import getch

def getpass(prompt="Digite sua senha: "):
    senha = ""
    print(prompt, end='', flush=True)
    while True:
        char = getch.getch()
        if char == '\r' or char == '\n':
            break
        elif char == '\x7f': 
                senha = senha[:-1]
                print('\b \b', end='', flush=True)
        else:
            senha += char
            print('*', end='', flush=True)
    print() 
    return senha


