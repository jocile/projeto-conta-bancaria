import sqlite3

conexao = sqlite3.connect('Banco.db')
cursor = conexao.cursor()


cursor.execute( '''  
    CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    ddd TEXT,
    numero TEXT,
    email TEXT,
    CEP TEXT,
    Ncasa TEXT,
    senha TEXT)
                ''' )


def Cadastro_db(nome, cpf, ddd, numero, email, CEP, Ncasa, senha):
    cursor.execute("INSERT INTO cliente (nome, cpf, ddd, numero, email, CEP, Ncasa, senha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, ddd, numero, email, CEP, Ncasa, senha))
    conexao.commit()
    print('Cadastro realizado com sucesso!')


def Login_db(cpf, senha):
    cursor.execute("SELECT * FROM cliente WHERE cpf =? AND senha =?", (cpf, senha))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False
    
def Fechar_db():
    conexao.close()