import sqlite3 
class Interface:
    pass
#1. criar usuário ou fazer login e enviar ou pesquisar as informações no banco de dados
#2. mostrar menu com opções de saque, depósito e mostrar o extrato
#3. Receber dados do depósito e mandar para a classe cliente
#4. Receber dados do saque e mandar para a classe cliente
#5. Receber informações do histórico e mostrar o extrato



class Cliente:
    def __init__(self) -> None:
        pass

    def cadastro(self):
        pass

    def login(self):
        pass

    def deposito(self):
        pass

    def saque(self):
        pass

    def extrato(self):
        pass



class Conta:
    def __init__(self, saldo, nome):
        self.saldo = saldo
        self.nome = self.nome_usuario()
        self.banco = Banco_de_dados()

    def nome_usuario(self):
        nome = self.banco.buscar_nome()
        return nome
    
    def saldo(self):
        pass


class Banco_de_dados:

    def cadastro(self): 
        pass

    def login(self):
        pass

    def deposito(self):
        pass

    def saque(self):
        pass

    def extrato(self):
        pass



def connect_db():
    try:
        conn = sqlite3.connect('banco.db')
        return conn
    except Error as e:
        print(e)
        return None

def criar_tabelas():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            saldo REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conta_id) REFERENCES contas (id)
        )
        ''')
        conn.commit()
        conn.close()

def adicionar_cliente(nome, sobrenome, cpf, email):
    if len(cpf) != 14:  # Verificação simplificada do CPF
        return 'Erro: CPF inválido'
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        
        # Verificar se o CPF já existe
        cursor.execute('''
        SELECT COUNT(*) FROM clientes WHERE cpf = ?
        ''', (cpf,))
        count = cursor.fetchone()[0]
        
        if count > 0:
            conn.close()
            return 'Erro: CPF já cadastrado'
        
        cursor.execute('''
        INSERT INTO clientes (nome, sobrenome, cpf, email)
        VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, cpf, email))
        conn.commit()
        conn.close()
        return 'Cliente adicionado com sucesso'
    return 'Erro ao conectar ao banco de dados'

def criar_conta(cliente_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO contas (cliente_id)
        VALUES (?)
        ''', (cliente_id,))
        conn.commit()
        conn.close()
        return 'Conta criada com sucesso'
    return 'Erro ao conectar ao banco de dados'

def realizar_transacao(conta_id, tipo, valor):
    if valor <= 0:
        return 'Erro: valor de transação inválido'
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO transacoes (conta_id, tipo, valor)
        VALUES (?, ?, ?)
        ''', (conta_id, tipo, valor))
        
        if tipo == 'deposito':
            cursor.execute('''
            UPDATE contas
            SET saldo = saldo + ?
            WHERE id = ?
            ''', (valor, conta_id))
        elif tipo == 'saque':
            # Verificar se há saldo suficiente antes de permitir o saque
            cursor.execute('''
            SELECT saldo FROM contas WHERE id = ?
            ''', (conta_id,))
            saldo_atual = cursor.fetchone()[0]
            if saldo_atual >= valor:
                cursor.execute('''
                UPDATE contas
                SET saldo = saldo - ?
                WHERE id = ?
                ''', (valor, conta_id))
            else:
                conn.close()
                return 'Erro: saldo insuficiente'
        
        conn.commit()
        conn.close()
        return 'Transação realizada com sucesso'
    return 'Erro ao conectar ao banco de dados'

def consultar_saldo(conta_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT saldo
        FROM contas
        WHERE id = ?
        ''', (conta_id,))
        saldo = cursor.fetchone()[0]
        conn.close()
        return saldo
    return 'Erro ao conectar ao banco de dados'

def listar_transacoes(conta_id):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM transacoes
        WHERE conta_id = ?
        ORDER BY data DESC
        ''', (conta_id,))
        transacoes = cursor.fetchall()
        conn.close()
        return transacoes
    return 'Erro ao conectar ao banco de dados'

# Criar tabelas ao iniciar
criar_tabelas()

# Exemplo de uso:
resultado = adicionar_cliente('João', 'Silva', '123.456.789-00', 'joao.silva@example.com')
print(resultado)  # Cliente adicionado com sucesso ou Erro: CPF já cadastrado

if resultado == 'Cliente adicionado com sucesso':
    criar_conta(1)
    realizar_transacao(1, 'deposito', 100.0)
    saldo = consultar_saldo(1)
    print(f'Saldo atual: {saldo}')
    realizar_transacao(1, 'saque', 50.0)
    transacoes = listar_transacoes(1)
    for transacao in transacoes:
        print(transacao)
