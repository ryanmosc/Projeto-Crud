import getpass
from hashlib import sha256
def logar(cursor):
    try:
        while True:
            nome_usuario = str(input("Digite o nome de usuario: ")).strip()
            if not nome_usuario:
                    raise ValueError("O nome não pode estar vazio.")
                            
            senha = getpass.getpass("Digite sua senha: ")
            if not senha:
                    raise ValueError("A senha não pode estar vazia.")
            hash_senha = sha256(senha.encode()).hexdigest()
            
            comando = f'SELECT * FROM usuarios WHERE nomes = %s and senhas = %s'
            cursor.execute(comando,(nome_usuario,hash_senha))
            resultado = cursor.fetchone()
            
            if resultado:
                print("Acesso liberado!")
                break
                                        
            else:
                print("Acesso negado!")
                print("Usuario ou senha invalida")
                logar(cursor)
            
    except Exception as e:
        print(f"Erro ao logar no sistema {e}")
    
    except ValueError as ve:
        print(f"Erro na entrada de dados: {ve}")
        logar(cursor)
        
    
      