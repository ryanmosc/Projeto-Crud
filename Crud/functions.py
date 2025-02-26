from colorama import Fore, Back, Style, init
import mysql.connector

def criar(cursor, conexao):
    try:
        print(Fore.YELLOW + "\n*** ADICIONAR PRODUTO ***")
        nome = input("Qual o nome do produto que deseja adicionar? ")
        valor = float(input("Qual o valor do produto? "))
        comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
        cursor.execute(comando, (nome, valor))
        conexao.commit()
        print(Fore.GREEN + "\nProduto adicionado com sucesso!")
    except ValueError:
        print(Fore.RED + "\nErro: Insira um valor numérico válido.")
    except mysql.connector.Error as e:
        print(Fore.RED + f"\nErro no banco de dados: {e}")
        conexao.rollback()

def ler_tabela(cursor):
    try:
        print(Fore.YELLOW + "\n*** VISUALIZAR PRODUTOS ***")
        comando = f'SELECT * FROM vendas;'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(Fore.CYAN + "\nProdutos cadastrados:")
        for row in resultado:
            print(Fore.GREEN + f"ID: {row[0]} | Produto: {row[1]} | Valor: R$ {row[2]:.2f}")
    except mysql.connector.Error as e:
        print(Fore.RED + f"\nErro no banco de dados: {e}")

def update(cursor, conexao):
    try:
        print(Fore.YELLOW + "\n*** ATUALIZAR PRODUTO ***")
        comando = 'SELECT * FROM vendas;'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(Fore.CYAN + "\nProdutos disponíveis para atualização:")
        if not resultado:
            print(Fore.YELLOW + "\nNenhum produto encontrado na base de dados.")
            return  
        for row in resultado:
            print(Fore.GREEN + f"ID: {row[0]} | Produto: {row[1]} | Valor: R$ {row[2]:.2f}")
        try:
            idUpdate = int(input("\nQual o ID do produto que deseja atualizar? "))
            if not idUpdate:
                raise ValueError("O ID do produto não pode ser vazio.")
        except ValueError:
            print(Fore.RED + "Erro: O ID do produto deve ser um número inteiro.")
            return
        
        comando = 'SELECT * FROM vendas WHERE idVendas = %s;'
        cursor.execute(comando, (idUpdate,))
        resultado = cursor.fetchone()  
        
        if not resultado:
            print(Fore.YELLOW + "\nNenhum produto encontrado com esse ID.")
            return
        
        while True:
            try:
                nome = input("Qual o novo nome do produto a ser atualizado ? ").strip()
                if not nome:
                    raise ValueError("O nome do produto não pode estar vazio")
                valor = float(input("Qual o  novo valor do produto a ser atualizado? R$ "))
                if valor < 0:
                    print("O valor do produto deve ser maior ou igual a 0")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Erro: os campos não podem ser deixados em branco.")
            except ValueError:
                print(Fore.RED + "Erro: Insira um valor numérico válido.")
        
        comando_update = 'UPDATE vendas SET nome_produto = %s, valor = %s WHERE idVendas = %s'
        cursor.execute(comando_update, (nome, valor, idUpdate))
        if cursor.rowcount == 0:
            print(Fore.YELLOW + "\nNenhum produto encontrado com esse ID.")
        else:
            conexao.commit()
            print(Fore.GREEN + "\nProduto atualizado com sucesso!")
    
    except ValueError as ve:
        print(Fore.RED + f"\nErro na entrada de dados: {ve}")
        conexao.rollback()
    except mysql.connector.Error as e:
        print(Fore.RED + f"\nErro no banco de dados: {e}")
        conexao.rollback()
    

def deletar(cursor, conexao):
    try:
        print(Fore.YELLOW + "\n*** REMOVER PRODUTO ***")
        idRemover = int(input('Qual o id do produto que deseja remover? '))
        comando = 'DELETE FROM vendas WHERE idVendas = %s'
        cursor.execute(comando, (idRemover,))
        conexao.commit()
        print(Fore.GREEN + "\nProduto removido com sucesso!")
    except ValueError as ve:
        print(Fore.RED + f"\nErro na entrada de dados: {ve}")
        conexao.rollback()