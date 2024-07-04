
class Dados_de_cadastro:
    
    especial = "!@#$%&*()_-+={[}]|\:;'<>?,./"

    def VerificNome(nome):
        try:
            nome = nome.strip().lower().title()
            if not nome:
                return 'Preencha esse campo', nome
            elif any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./"  for char in nome) or any(char.isnumeric() for char in nome) or len(nome) < 3:
                return 'Nome inválido', nome
            else:
                return '  ', nome
        except AttributeError:
            return 'Erro', nome

        
    def VerificCPF(cpf):
        try:
            if any(char in "!@#$%&*()_-+={[}]|\:;'<>?,./" for char in cpf) or any(char.isalpha() for char in cpf) or len(cpf)!= 11:
                return 'CPF inválido', cpf
            else:
                return 'ok', cpf
        except AttributeError:
            return 'Erro', cpf



    def VerificDDD(ddd):
        pass

    def VerificNumero(numero):
        pass

    def VerificEmail(email):
        pass

    def VerificDepartamento(departamento):
        pass

    def VerificCargo(cargo):
        pass

    def VerificSenha(senha):
        pass

    def VerificConfirmSenha(ConfirmSenha):
        pass