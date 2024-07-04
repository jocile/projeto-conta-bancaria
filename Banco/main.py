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


class Supermercado(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        sm.add_widget(Screen_Menu(name='menu'))
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
                self.manager.current = 'menu'
            else:
                self.ids.verificacao_log_error.text = 'Dados incorretos'

    def tela_login(self, departamento):
        self.manager.current = departamento


class Screen_Cadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def informacoes_de_cadastro(self, nome, cpf, ddd, numero, email, CEP, Ncasa, senha, ConfirmSenha):
        Erros = ['Preencha esse campo', 'Nome inválido', 'CPF inválido', 'DDD inválido', 'Número inválido', 'E-mail inválido', 'CEP inválido', 'Senha inválida',
                 'Erro', 'A senha deve ter pelo menos 6 digitos', 'As senhas não coincidem', 'Selecione uma opção']
        Verific = ["ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]
        Verific[0], nome_db = cadastro_login.VerificNome(nome)
        self.ids.nome_cad_error.text = Verific[0]
        Verific[1], cpf_db = cadastro_login.VerificCPF(cpf)
        self.ids.cpf_cad_error.text = Verific[1]
        Verific[2], ddd_db, numero_db = cadastro_login.VerificDDDNumero(ddd, numero)
        self.ids.DDDnumero_cad_error.text = Verific[2]
        Verific[3], email_db = cadastro_login.VerificEmail(email)
        self.ids.email_cad_error.text = Verific[3]
        Verific[4], CEP_db = cadastro_login.VerificCEP(CEP)
        self.ids.CEP_cad_error.text = Verific[4]
        Verific[5], Ncasa_db = cadastro_login.VerificNcasa(Ncasa)
        self.ids.Ncasa_cad_error.text = Verific[5]
        Verific[6], senha_db = cadastro_login.VerificSenha(senha)
        self.ids.senha_cad_error.text = Verific[6]
        Verific[7], ConfirmSenha_db = cadastro_login.VerificConfirmSenha(ConfirmSenha, senha)
        self.ids.confirmSenha_cad_error.text = Verific[7]

        if not any(erro in Erros for erro in Verific):
                banco_de_dados.Cadastro_db(nome_db, cpf_db, ddd_db, numero_db, email_db, CEP_db, Ncasa_db, senha_db)
                self.ids.verificacao_cad_error.text = 'Cadastro realizado com sucesso\nVolte e realize o login'


class Screen_Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



Supermercado().run()
banco_de_dados.Fechar_db()