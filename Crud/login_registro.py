import mysql.connector
from colorama import Fore, Back, Style, init
from login import logar
from registro import registro

def login_registro(cursor, conexao):
    while True:
        try:
            print(Fore.CYAN + "\n*** LOGIN E REGISTRO ***\n")
            escolha = int(input(Fore.GREEN + "Deseja entrar ou se registrar? [1] Entrar [2] Registrar: "))
            if escolha == 1:
                logar(cursor)
                break
            elif escolha == 2:
                registro(cursor,conexao)
                break
            else:
                print("Escolha uma opção válida [1] para fazer Login e [2] para se registrar:")
                
        except ValueError:
                print(Fore.RED + "Erro: Digite um número válido!")
        except mysql.connector.Error as e:
            print(Fore.RED + f"Erro no banco de dados: {e}")
            break  
        except Exception as e:
            print(Fore.RED + f"Erro inesperado: {e}")
            break  