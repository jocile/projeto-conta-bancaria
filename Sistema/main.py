import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.core.window import Window
import cadastro_login
import banco_de_dados

cliente = {'nome': '', 'cpf': '', 'ddd': '', 'numero': '', 'email': '', 'data': '', 'CEP': '', 'rua': '', 'Ncasa': '','senha': '','saldo': 0}


class Sistema_Bancario(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        sm.add_widget(Screen_Menu(name='menu'))
        sm.add_widget(Screen_Deposito(name='deposito'))
        sm.add_widget(Screen_Saque(name='saque'))
        sm.add_widget(Screen_Extrato(name='extrato'))
        sm.add_widget(Screen_Perfil(name='perfil'))
        return Builder.load_file('Tela.kv')


class Screen_Login(Screen):
    def informacoes_de_login(self, cpf, senha):
        Verific = [' ', '', '']
        Verific[0], cpf_log = cadastro_login.VerificCPF(cpf)
        self.ids.cpf_log_error.text = Verific[0]
        Verific[1], senha_log = cadastro_login.VerificSenha(senha)
        self.ids.senha_log_error.text = Verific[1]

        if any(verif == ' ' for verif in Verific):
            verificacao = banco_de_dados.Login_db(cpf, senha)
            if verificacao:
                self.ids.verificacao_log_error.text = ''
                self.ids.cpf_log_error.text = ''
                self.ids.cpf_log.text = ''
                self.ids.senha_log_error.text = ''
                self.ids.senha_log.text = ''
                self.Salvar_cliente(cpf)
                self.manager.current = 'menu'
            else:
                self.ids.verificacao_log_error.text = 'Dados incorretos'

    def Salvar_cliente(self, cpf):
        cliente_info = banco_de_dados.Informacoes_db(cpf)
        cliente['nome'] = cliente_info[0]
        cliente['cpf'] = cliente_info[1]
        cliente['ddd'] = cliente_info[2]
        cliente['numero'] = cliente_info[3]
        cliente['email'] = cliente_info[4]
        cliente['data'] = cliente_info[5]
        cliente['CEP'] = cliente_info[6]
        cliente['rua'] = cliente_info[7]
        cliente['Ncasa'] = cliente_info[8]
        cliente['senha'] = cliente_info[9]
        cliente['saldo'] = cliente_info[10]


class Screen_Cadastro(Screen):
    def informacoes_de_cadastro(self, nome, cpf, ddd, numero, email, data, cep, rua, Ncasa, senha, ConfirmSenha):
        Erros = ['Preencha esse campo', 'Nome inválido', 'CPF inválido', 'DDD inválido', 'Número inválido', 'E-mail inválido', 'CEP inválido', 'Rua inválida', 'Senha inválida',
                 'Erro', 'A senha deve ter pelo menos 8 digitos', 'As senhas não coincidem', 'Selecione uma opção']

        Verific = ["ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]
        Verific[0], nome_db = cadastro_login.VerificNome(nome)
        self.ids.nome_cad_error.text = Verific[0]
        Verific[1], cpf_db = cadastro_login.VerificCPF(cpf)
        self.ids.cpf_cad_error.text = Verific[1]
        Verific[2], ddd_db, numero_db = cadastro_login.VerificDDDNumero(ddd, numero)
        self.ids.DDDnumero_cad_error.text = Verific[2]
        Verific[3], email_db = cadastro_login.VerificEmail(email)
        self.ids.email_cad_error.text = Verific[3]
        Verific[4], data_db = cadastro_login.VerificData(data)
        self.ids.data_cad_error.text = Verific[4]
        Verific[5], cep_db = cadastro_login.VerificCEP(cep)
        self.ids.cep_cad_error.text = Verific[5]
        Verific[6], rua_db = cadastro_login.VerificRua(rua)
        self.ids.rua_cad_error.text = Verific[6]
        Verific[7], Ncasa_db = cadastro_login.VerificNcasa(Ncasa)
        self.ids.Ncasa_cad_error.text = Verific[7]
        Verific[8], senha_db = cadastro_login.VerificSenha(senha)
        self.ids.senha_cad_error.text = Verific[8]
        Verific[9], ConfirmSenha_db = cadastro_login.VerificConfirmSenha(ConfirmSenha, senha)
        self.ids.confirmSenha_cad_error.text = Verific[9]

        if not any(erro in Erros for erro in Verific):
            banco_de_dados.Cadastro_db(nome_db, cpf_db, ddd_db, numero_db, email_db, data_db, cep_db, rua_db, Ncasa_db, senha_db)
            self.ids.verificacao_cad_error.text = 'Cadastro realizado com sucesso'


class Screen_Menu(Screen):
    def on_enter(self, *args):
        self.ids.nome_menu.text = f"Nome: {cliente['nome']}"
        self.ids.cpf_menu.text = f"CPF: {cliente['cpf'][:3] + '.' + cliente['cpf'][3:6] + '.' + cliente['cpf'][6:9] + '-' + cliente['cpf'][9:]}"
        self.ids.numero_menu.text = f"Número: ({cliente['ddd']}) {cliente['numero'][:5]}-{cliente['numero'][5:]}"
        self.ids.email_menu.text = f"E-mail: {cliente['email']}"
        self.ids.data_menu.text = f"Data de nascimento: {cliente['data'][:2]}/{cliente['data'][2:4]}/{cliente['data'][4:]}"
        self.ids.cep_menu.text = f"CEP: {cliente['CEP'][:5]}{cliente['CEP'][5:]}"
        self.ids.rua_menu.text = f"{cliente['rua']}"
        self.ids.casa_menu.text = f"Número da casa: {cliente['Ncasa']}"
        self.ids.saldo_menu.text = f"Saldo: R$ {cliente['saldo']:.2f}"


class Screen_Deposito(Screen):
    def on_enter(self, *args):
        self.ids.saldo_deposito.text = f"Saldo: R$ {cliente['saldo']:.2f}"

    def Depositar(self, valor):
        saldo = cliente['saldo']
        if not valor:
            self.ids.deposito_error.text = 'Preencha o valor do depósito'
        elif not valor.isnumeric():
            self.ids.deposito_error.text = 'Digite um valor válido'
        elif float(valor) <= 0:
            self.ids.deposito_error.text = 'Valor inválido'
        else:
            cliente['saldo'] += float(valor)
            banco_de_dados.Deposito(cliente['cpf'], cliente['saldo'])
            banco_de_dados.Adicionar_transacao(cliente['cpf'], 'Depósito', valor)
            self.ids.deposito_error.text = ''
            self.manager.current = 'menu'


class Screen_Saque(Screen):
    def on_enter(self, *args):
        self.ids.saldo_saque.text = f"Saldo: R$ {cliente['saldo']:.2f}"

    def Sacar(self, valor):
        saldo = cliente['saldo']
        if not valor:
            self.ids.saque_error.text = 'Preencha o valor do saque'
        elif not valor.isnumeric():
            self.ids.saque_error.text = 'Digite um valor válido'
        elif float(saldo) < float(valor):
            self.ids.saque_error.text = 'Saldo insuficiente'
        elif float(valor) <= 0:
            self.ids.saque_error.text = 'Valor inválido'
        else:
            cliente['saldo'] -= float(valor)
            banco_de_dados.Saque(cliente['cpf'], cliente['saldo'])
            banco_de_dados.Adicionar_transacao(cliente['cpf'], 'Saque', valor)
            self.ids.saque_error.text = ''
            self.ids.saque.text = ''
            self.manager.current = 'menu'


class Screen_Extrato(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Screen_Perfil(Screen):
    def on_enter(self, *args):
        self.ids.nome_menu_alterar.text = f"Nome: {cliente['nome']}"
        self.ids.cpf_menu_alterar.text = f"CPF: {cliente['cpf'][:3] + '.' + cliente['cpf'][3:6] + '.' + cliente['cpf'][6:9] + '-' + cliente['cpf'][9:]}"
        self.ids.numero_menu_alterar.text = f"Número: ({cliente['ddd']}) {cliente['numero'][:5]}-{cliente['numero'][5:]}"
        self.ids.email_menu_alterar.text = f"E-mail: {cliente['email']}"
        self.ids.data_menu_alterar.text = f"Data de nascimento: {cliente['data'][:2]}/{cliente['data'][2:4]}/{cliente['data'][4:]}"
        self.ids.cep_menu_alterar.text = f"CEP: {cliente['CEP'][:5]}{cliente['CEP'][5:]}"
        self.ids.rua_menu_alterar.text = f"{cliente['rua']}"
        self.ids.casa_menu_alterar.text = f"Número da casa: {cliente['Ncasa']}"
        self.ids.saldo_menu_alterar.text = f"Saldo: R$ {cliente['saldo']:.2f}"

    def Alterar_perfil(self, ddd, numero, email, cep, rua, Ncasa):
        Erros = ['DDD inválido', 'Número inválido', 'E-mail inválido', 'CEP inválido', 'Rua inválida', 'Preencha o Número', 'Preencha o DDD', 'Erro']
        Verific = ["ok", "ok", "ok", "ok", "ok"]

        Verific[0], ddd_db, numero_db = cadastro_login.VerificDDDNumeroAlterar(ddd, numero)
        self.ids.DDDnumero_alterar_error.text = Verific[0]
        Verific[1], email_db = cadastro_login.VerificEmailAlterar(email)
        self.ids.email_alterar_error.text = Verific[1]
        Verific[2], cep_db = cadastro_login.VerificCEPAlterar(cep)
        self.ids.cep_alterar_error.text = Verific[2]
        Verific[3], rua_db = cadastro_login.VerificRuaAlterar(rua)
        self.ids.rua_alterar_error.text = Verific[3]
        Verific[4], Ncasa_db = cadastro_login.VerificNcasaAlterar(Ncasa)
        self.ids.casa_alterar_error.text = Verific[4]

        if not any(erro in Erros for erro in Verific):
            banco_de_dados.Atualizar_Perfil(ddd_db, numero_db, email_db, cep_db, rua_db, Ncasa_db, cliente['cpf'])
            if ddd_db: cliente['ddd'] = ddd_db
            if numero_db: cliente['numero'] = numero_db
            if email_db: cliente['email'] = email_db
            if cep_db: cliente['CEP'] = cep_db
            if rua_db: cliente['rua'] = rua_db
            if Ncasa_db: cliente['Ncasa'] = Ncasa_db
            self.ids.ddd_alterar.text = ''
            self.ids.numero_alterar.text = ''
            self.ids.email_alterar.text = ''
            self.ids.cep_alterar.text = ''
            self.ids.rua_alterar.text = 'Rua '
            self.ids.casa_alterar.text = ''
            self.ids.DDDnumero_alterar_error.text = ''
            self.ids.email_alterar_error.text = ''
            self.ids.cep_alterar_error.text = ''
            self.ids.rua_alterar_error.text = ''
            self.ids.casa_alterar_error.text = ''
            self.manager.current = 'menu'


Sistema_Bancario().run()
banco_de_dados.Fechar_db()
