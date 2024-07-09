# Projeto Conta Bancaria
---

**Caio:** desenvolvedor front-end e Data Base 
**Alisson:** Líder de equipe 
**Pedro:** Desenvolvedor Back-end  
**Gabriel:** Desenvolvedor Back-end  
**Natanael:** Desenvolvedor Data Base 
**Silas:** desenvolvedor back-end

---

## Descrição do Projeto:  
Projeto integrador do curso *programador de sistemas* - SENAC
O projeto tem intuito desenvolver um software de sistema bancário.
O sistema é dividido em 2 partes:
1. Conta do usuário
2. operações do usuário

---


## Fluxograma do projeto:
![fluxograma](https://github.com/osmozeInc/projeto-conta-bancaria/assets/120123623/07aa3120-c0c0-4a9e-a287-0f39e69a8619)

O sistema deve ter 4 divisões:
1. Conta
2. Cliente
3. Banco de dados
4. Interface
---

A Interface deve ter a opção de:
criar usuário ou fazer login e enviar ou pesquisar as informações no banco de dados
mostrar menu com opções de saque, depósito e mostrar o extrato
Receber dados do depósito e mandar para a classe cliente
Receber dados do saque e mandar para a classe cliente
Receber informações do histórico e mostrar o extrato


A classe Cliente deve fazer
cadastro:
receber nome, cpf, numero, email e idade do usuário e senha
chamar a função do banco de dados e enviar os dados


login:
receber cpf e senha
chamar a função para verificar os dados no banco de dados


depósito:
receber valor do depósito,
verifica se o valor é valido e retorna nada, ou uma mensagem de erro para a tela
o depósito chama a função de alterar o saldo
o depósito chama a função de adicionar algo ao hitórico


saque:
receber valor do saque,
verifica se o valor é valido e retorna nada se for válido, ou uma mensagem de erro para a tela caso não seja
o saque chama a função de alterar o saldo
o saque chama a função de adicionar algo ao hitórico


extrato:
chama a função que retorna os dados de cada transação
envia os dados para a tela



A classe conta deve ter:
variavel privada saldo
nome do usuário


função para pegar nome do usuário no banco de dados
funçâo para alterar o valor do saldo e registrar mudança no banco de dados



A classe banco de dados deve fazer:
cadastro:
criar tabela e guardar nome, cpf, numero, email e idade do usuário e senha
cria uma tabela para o extrato do usuário


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
