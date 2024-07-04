import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.core.window import Window
import dados


class Banco_de_Dados:
    def __init__(self):
        self.conexao = sqlite3.connect('Supermercado.db')
        self.cursor = self.conexao.cursor()

    def Criar_tabelas(self):
        pass

    def Cadastro_db(self, nome, cpf, numero, email, departamento, função, senha):
        nome_db = nome


class Supermercado(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        return Builder.load_file('Tela.kv')


class Screen_Login(Screen):        
    def get_input_login(self, cpf, senha, departamento):
        pass   


class Screen_Cadastro(Screen, Banco_de_Dados):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        banco = Banco_de_Dados()
    
    def informacoes_de_cadastro(self, nome, cpf, ddd, numero, email, departamento, função, senha, ConfirmSenha):
        Verific = [" ", " ", " ", " ", " ", " ", " ", " "]
        Verific[0], nome_db = dados.Dados_de_cadastro.VerificNome(nome)
        if Verific[0] != ' ': self.ids.nome_cad_error.text = Verific[0]
        Verific[1], cpf_db = dados.Dados_de_cadastro.VerificCPF(cpf)
        '''if Verific[1] != ' ': self.ids.cpf_cad_error.text = Verific[1]
        Verific[2], ddd_db, numero_db = dados.Dados_de_cadastro.VerificDDDNumero(ddd, numero)
        if Verific[2] != ' ': self.ids.DDDnumero_cad_error.text = Verific[2]
        Verific[3], email_db = dados.Dados_de_cadastro.VerificEmail(email)
        if Verific[3] != ' ': self.ids.email_cad_error.text = Verific[3]
        Verific[4], departamento_db = dados.Dados_de_cadastro.VerificDepartamento(departamento)
        if Verific[4] != ' ': self.ids.departamento_cad_error.text = Verific[4]
        Verific[5], função_db = dados.Dados_de_cadastro.VerificCargo(função)
        if Verific[5] != ' ': self.ids.cargo_cad_error.text = Verific[5]'''
        '''Verific[7], senha_db = dados.Dados_de_cadastro.VerificSenha(senha)
        if Verific[7] != 'ok': self.ids.senha_cad_error.text = Verific[7]
        Verific[8], ConfirmSenha_db = dados.Dados_de_cadastro.VerificConfirmSenha(ConfirmSenha)
        if Verific[8] != 'ok': self.ids.ConfirmSenha_cad_error.text = Verific[8]'''

        for verific in Verific:
            if verific != 'Erro':
                pass

    

    def spinner_funcao(self, departamento, value):
        if value == 'Entrega':
            self.ids.cargo_cad.values = ('Entregador',)
        elif value == 'Cozinha':
            self.ids.cargo_cad.values = ('Açougueiro', 'Padeiro', 'Peixero', 'Cozinheiro', 'Sommelier de vinhos')
        elif value == 'Atendimento':
            self.ids.cargo_cad.values = ('Operador de caixa', 'Empacotador')
        elif value == 'Estoque':
            self.ids.cargo_cad.values = ('Repositor', 'Estoquista')
        elif value == 'Administração':
            self.ids.cargo_cad.values = ('Gerente', 'Auxiliar administrativo')
        elif value == 'Auxiliar':
            self.ids.cargo_cad.values = ('Segurança,', 'Limpeza')
        else:
            self.ids.cargo_cad.values = ()


banco = Banco_de_Dados()
Supermercado().run()
