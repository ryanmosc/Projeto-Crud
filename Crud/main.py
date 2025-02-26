import mysql.connector
from login import logar
from registro import registro
from colorama import Fore, Back, Style, init
from functions import criar, ler_tabela, update, deletar
from login_registro import login_registro


# Inicializa o colorama
init(autoreset=True)

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Insira sua senha',
    database='Insira seu banco de dados'
)
cursor = conexao.cursor()





def main():
    login_registro(cursor, conexao)

    while True:
        try:
            print(Fore.CYAN + "\n*** BEM VINDO AO CRUD DE PRODUTOS ***")
            print(Fore.YELLOW + "\nEscolha uma das opções abaixo:")
            print(Fore.GREEN + "[1] Adicionar produto")
            print(Fore.GREEN + "[2] Ver produtos cadastrados")
            print(Fore.GREEN + "[3] Atualizar produto")
            print(Fore.GREEN + "[4] Remover produto")
            print(Fore.RED + "[5] Sair")
            
            opcao = int(input(Fore.BLUE + "\nEscolha a opção: "))

            if opcao == 1:
                criar(cursor, conexao)
            elif opcao == 2:
                ler_tabela(cursor)
            elif opcao == 3:
                update(cursor, conexao)
            elif opcao == 4:
                deletar(cursor, conexao)
            elif opcao == 5:
                print(Fore.GREEN + "\nSaindo... Até logo!")
                break  
            else:
                print(Fore.RED + "\nEscolha uma opção válida.")
        except ValueError as ve:
            print(Fore.RED + f"\nEscolha um valor válido [1] [2] [3] [4] [5]: {ve}")
        except mysql.connector.Error as e:
            print(Fore.RED + f"\nErro ao conectar ao banco de dados: {e}")
        except Exception as e:
            print(Fore.RED + f"\nOcorreu um erro inesperado: {e}")

    cursor.close()
    conexao.close()

if __name__ == '__main__':
    main()
