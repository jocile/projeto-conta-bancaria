import re

def VerificNome(nome):
    try:
        nome = nome.strip().lower().title()
        if not nome:
            return 'Preencha esse campo', nome
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./"  for char in nome) or any(char.isnumeric() for char in nome) or len(nome) < 3:
            return 'Nome inválido', nome
        else:
            return ' ', nome
    except AttributeError:
        return 'Erro', nome

def VerificCPF(cpf):
    try:
        if not cpf:
            return 'Preencha esse campo', cpf
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in cpf) or any(char.isalpha() for char in cpf) or len(cpf)!= 11:
            return 'CPF inválido', cpf
        else:
            return ' ', cpf
    except AttributeError:
        return 'Erro', cpf

def VerificDDDNumero(ddd, numero):
    try:
        if not ddd or not numero:
            return 'Preencha esse campo', ddd, numero
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in ddd) or any(char.isalpha() for char in ddd) or len(ddd)!= 2:
            return "DDD invalido!", ddd, numero
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in numero) or any(char.isalpha() for char in numero) or len(numero)!= 9:
            return "Numero invalido!", ddd, numero
        else:
            return ' ', ddd, numero
    except AttributeError:
        return 'Erro', ddd, numero

def VerificEmail(email):
    email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not email:
        return 'Preencha esse campo', email
    elif not re.match(email_padrao, email):
        return 'Email inválido', email
    else:
        return ' ', email

def VerificCEP(CEP):
    if not CEP:
        return 'Preencha esse campo', CEP
    elif len(CEP) != 8 or not CEP.isnumeric():
        return 'CEP inválido', CEP
    else:
        return ' ', CEP

def VerificNcasa(Ncasa):
    if not Ncasa:
        return 'Preencha esse campo', Ncasa
    elif not Ncasa.isnumeric():
        return 'Numero inválido', Ncasa
    else:
        return ' ', Ncasa

def VerificSenha(senha):
    if not senha:
        return 'Preencha esse campo', senha
    elif len(senha) < 8:
        return 'A senha deve ter pelo menos 6 digitos', senha
    else:
        return ' ', senha

def VerificConfirmSenha(ConfirmSenha, senha):
    if not ConfirmSenha:
        return 'Preencha esse campo', ConfirmSenha
    elif ConfirmSenha != senha:
        return 'As senhas não coincidem', ConfirmSenha
    else:
        return ' ', ConfirmSenha