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
            return "DDD inválido!", ddd, numero
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in numero) or any(char.isalpha() for char in numero) or len(numero)!= 9:
            return "Numero inválido!", ddd, numero
        else:
            return ' ', ddd, numero
    except AttributeError:
        return 'Erro', ddd, numero


def VerificEmail(email):
    email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not email:
        return 'Preencha esse campo', email
    elif not re.match(email_padrao, email):
        return 'E-mail inválido', email
    else:
        return ' ', email


def VerificData(data):
        data = data.strip().lower().title()
        if not data:
            return 'Preencha esse campo', data
        elif len(data) != 10 or data.isalpha() or not data[2] == '/' or not data[5] == '/':
            return 'Data inválida', data
        else:
            return ' ', data[:2] + data[3:5] + data[6:]


def VerificCEP(CEP):
    if not CEP:
        return 'Preencha esse campo', CEP
    elif len(CEP) != 8 or not CEP.isnumeric():
        return 'CEP inválido', CEP
    else:
        return ' ', CEP


def VerificRua(rua):
    if not rua:
        return 'Preencha esse campo', rua
    elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in rua) or len(rua) < 3:
        return 'Rua inválida', rua[4:]
    else:
        return ' ', rua.title()


def VerificNcasa(Ncasa):
    if not Ncasa:
        return 'Preencha esse campo', Ncasa
    elif not Ncasa.isnumeric():
        return 'Número inválido', Ncasa
    else:
        return ' ', Ncasa


def VerificSenha(senha):
    if not senha:
        return 'Preencha esse campo', senha
    elif len(senha) < 8:
        return 'A senha deve ter pelo menos 8 digitos', senha
    else:
        return ' ', senha


def VerificConfirmSenha(ConfirmSenha, senha):
    if not ConfirmSenha:
        return 'Preencha esse campo', ConfirmSenha
    elif ConfirmSenha != senha:
        return 'As senhas não coincidem', ConfirmSenha
    else:
        return ' ', ConfirmSenha
    



def VerificDDDNumeroAlterar(ddd, numero):
    try:
        if not ddd and not numero:
            return ' ', ddd, numero
        elif not ddd and numero:
            return "Preencha o DDD", ddd, numero
        elif not numero:
            return "Preencha o Número", ddd, numero
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in ddd) or any(char.isalpha() for char in ddd) or len(ddd)!= 2:
            return "DDD inválido", ddd, numero
        elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in numero) or any(char.isalpha() for char in numero) or len(numero)!= 9:
            return "Número inválido", ddd, numero
        else:
            return ' ', ddd, numero
    except AttributeError:
        return 'Erro', ddd, numero


def VerificEmailAlterar(email):
    email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not email:
        return ' ', email
    elif not re.match(email_padrao, email):
        return 'E-mail inválido', email
    else:
        return ' ', email


def VerificCEPAlterar(cep):
    if not cep:
        return ' ', cep
    elif len(cep) != 8 or not cep.isnumeric():
        return 'CEP inválido', cep
    else:
        return ' ', cep


def VerificRuaAlterar(rua):
    if not rua or rua == 'Rua ':
        rua = ""
        return ' ', rua
    elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in rua) or len(rua) < 3:
        return 'Rua inválida', rua[4:]
    else:
        return ' ', rua.title()
    
   
def VerificNcasaAlterar(Ncasa):
    if not Ncasa:
        return ' ', Ncasa
    elif not Ncasa.isnumeric():
        return 'Número inválido', Ncasa
    else:
        return ' ', Ncasa
