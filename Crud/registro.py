import mysql.connector
from hashlib import sha256
from login import logar
import re
def registro(cursor,conexao):
    while True:
            try:
                nome = (input("Qual o nome do que deseja adicionar?")).strip()
                if not nome:
                    raise ValueError("O nome não pode estar vazio.")
                
        
                
                email = (input("Qual o email do que deseja adicionar?"))
                
                verifica_email = 'SELECT * FROM usuarios WHERE enails = %s'
                cursor.execute(verifica_email, (email,))
                comparacao = cursor.fetchall()
                if comparacao:
                    print("Email já cadastrado")
                    continue
                                
                if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
                    print("Email inválido. Use um formato válido (ex.: usuario@dominio.com)")
                    continue
                
                       
                
                senha = (input("Qual sua senha?"))
                execao_senha = len(senha)
                if execao_senha < 8:
                    print("Senha muito curta (minimo 8 caracteres)")
                    continue
                else:
                    senha_armazenar = sha256(senha.encode()).hexdigest()

                comando = "INSERT INTO usuarios (nomes, enails, senhas) VALUES (%s, %s, %s)"
                cursor.execute(comando, (nome, email, senha_armazenar))
                conexao.commit() 
                print("Usuario cadastrado com sucesso")
                logar(cursor)
                break
                
            except mysql.connector.Error as e:
                print(f"Erro no banco de dados: {e}")
                conexao.rollback()
            except ValueError as ve:
                print(f"Erro na entrada de dados: {ve}")
            
            except Exception as e:
                print(f"Erro inesperado ao cadastrar o usuário: {e}")