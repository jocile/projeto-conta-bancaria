# Projeto Conta Bancaria
---

1. **Caio:** desenvolvedor front-end e Data Base 
2. **Alisson:** Líder de equipe 
3. **Pedro:** Desenvolvedor Back-end  
4. **Gabriel:** Desenvolvedor Back-end  
5. **Natanael:** Desenvolvedor Data Base 
6. **Silas:** desenvolvedor back-end

---

# Descrição do Projeto:  
Projeto integrador do curso *programador de sistemas* - SENAC
O projeto tem intuito desenvolver um software de sistema bancário.
O sistema é dividido em 2 partes:
1. Conta do usuário
2. operações do usuário

---


# Fluxograma do projeto:
![fluxograma](https://github.com/osmozeInc/projeto-conta-bancaria/assets/120123623/07aa3120-c0c0-4a9e-a287-0f39e69a8619)

## O sistema deve ter 4 divisões:
1. Conta
2. Cliente
3. Banco de dados
4. Interface
---

# A classe conta deve ter:
1. variavel privada 
2. saldo
3. nome do usuário
---


# A classe Cliente deve fazer:
1. cadastro (receber nome, cpf, numero, email e idade do usuário e senha
chamar a função do banco de dados e enviar os dados).

---

# A classe banco de dados deve fazer:
Cadastro (criar tabela e guardar nome, cpf, numero, email e idade do usuário e senha
cria uma tabela para o extrato do usuário)


login:
receber cpf e senha e verificar os dados no banco de dados
retornar true ou false se existir ou não


depósito:
receber valor do depósito e nome do usuário e atualizar na tabela dele
adicionar a operação realizada na tabela do extrato


saque:
receber valor do saque e nome do usuário e atualizar na tabela dele
adicionar a operação realizada na tabela do extarto


extrato:
retorna todos as operações da tabela extrato

# A Interface deve ter a opção de:

## Login:
 Receber cpf e senha
 Chamar a função para verificar os dados no banco de dados


## Depósito:
Receber valor do depósito,
verifica se o valor é valido e retorna nada, ou uma mensagem de erro para a tela
o depósito chama a função de alterar o saldo
o depósito chama a função de adicionar algo ao hitórico


## Saque:
receber valor do saque,
verifica se o valor é valido e retorna nada se for válido, ou uma mensagem de erro para a tela caso não seja
o saque chama a função de alterar o saldo
o saque chama a função de adicionar algo ao hitórico


## Extrato:
chama a função que retorna os dados de cada transação
envia os dados para a tela




função para pegar nome do usuário no banco de dados
funçâo para alterar o valor do saldo e registrar mudança no banco de dados

---



# Diagrama de casos de uso

![diagrama](https://github.com/osmozeInc/projeto-conta-bancaria/assets/168863507/32c839cd-bf58-4b70-9445-b0c094c480b0)
