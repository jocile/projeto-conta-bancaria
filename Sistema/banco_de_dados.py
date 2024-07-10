import sqlite3

conexao = sqlite3.connect('Banco.db')
cursor = conexao.cursor()


cursor.execute( '''  
    CREATE TABLE IF NOT EXISTS cliente 
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT UNIQUE,
    ddd TEXT,
    numero TEXT,
    email TEXT,
    data TEXT,
    CEP TEXT,
    rua TEXT,
    Ncasa TEXT,
    senha TEXT,
    saldo INTEGER
    )
    ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS extrato 
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    tipo TEXT,
    valor REAL,
    FOREIGN KEY(cliente_id) REFERENCES cliente(id)
    )
    ''')

def Cadastro_db(nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha):
    cursor.execute("INSERT INTO cliente (nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha, saldo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha, 0))
    conexao.commit()
    print('Cadastro realizado com sucesso!')


def Login_db(cpf, senha):
    if not cpf or not senha:
        return False
    
    cursor.execute("SELECT * FROM cliente WHERE cpf =? AND senha =?", (cpf, senha))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False


def Atualizar_Perfil(ddd, numero, email, cep, rua, Ncasa, cpf):
    cursor.execute("UPDATE cliente SET ddd =?, numero =?, email =?, CEP =?, rua =?, Ncasa =? WHERE cpf =?", (ddd, numero, email, cep, rua, Ncasa, cpf))


def Atualizar_Saldo(cpf):
    cursor.execute("SELECT saldo FROM cliente WHERE cpf =?", (cpf,))
    result = cursor.fetchone()
    
    if result:
        saldo = result[0]
        print('Saldo atualizado: ', saldo)
        return saldo
    else:
        return False


def Informacoes_db(cpf):
    cursor.execute("SELECT nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha, saldo FROM cliente WHERE cpf =?", (cpf,))
    result = cursor.fetchall()
    if result:
        return result[0]
    else:
        return False


def Saque(cpf, saldo):
    cursor.execute("UPDATE cliente SET saldo = ? WHERE cpf = ?", (saldo, cpf))


def Deposito(cpf, saldo):
    cursor.execute("UPDATE cliente SET saldo = ? WHERE cpf = ?", (saldo, cpf))


def Adicionar_Opreracao(cpf, tipo, valor):
    cursor.execute("SELECT id FROM cliente WHERE cpf = ?", (cpf,))
    result = cursor.fetchone()

    if result:
        id = result[0]
        cursor.execute("INSERT INTO extrato (cliente_id, tipo, valor) VALUES (?,?,?)", (id, tipo, valor))
        conexao.commit()
    else:
        return False
    

def Extrato(cpf):
    cursor.execute("SELECT id FROM cliente WHERE cpf = ?", (cpf,))
    result = cursor.fetchone()

    if result:
        id = result[0]
        cursor.execute("SELECT tipo, valor FROM extrato WHERE cliente_id =?", (id,))
        extrato = cursor.fetchall()
        return extrato
    else:
        return False


def Fechar_db():
    conexao.commit()
    conexao.close()
