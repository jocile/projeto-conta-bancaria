O sistema deve ter 4 divisões:

1. Conta
2. Cliente
3. Banco de dados
4. Interface


## A Interface deve ter a opção de:
1. criar usuário ou fazer login e enviar ou pesquisar as informações no banco de dados
2. mostrar menu com opções de saque, depósito e mostrar o extrato
3. Receber dados do depósito e mandar para a classe cliente
4. Receber dados do saque e mandar para a classe cliente
5. Receber informações do histórico e mostrar o extrato  
---
<br>
<br>


## A classe Cliente deve fazer

**cadastro:**  
receber nome, cpf, numero, email e idade do usuário e senha  
chamar a função do banco de dados e enviar os dados  
<br>

**login:**  
receber cpf e senha  
chamar a função para verificar os dados no banco de dados  
<br>

**depósito:**  
receber valor do depósito,  
verifica se o valor é valido e retorna nada, ou uma mensagem de erro para a tela  
o depósito chama a função de alterar o saldo  
o depósito chama a função de adicionar algo ao hitórico  
<br>

**saque:**  
receber valor do saque,  
verifica se o valor é valido e retorna nada se for válido, ou uma mensagem de erro para a tela caso não seja  
o saque chama a função de alterar o saldo  
o saque chama a função de adicionar algo ao hitórico  
<br>

**extrato:**  
chama a função que retorna os dados de cada transação  
envia os dados para a tela  

---
<br>
<br>



## A classe conta deve ter:
variavel privada saldo  
nome do usuário  
<br>

função para pegar nome do usuário no banco de dados
<br>
funçâo para alterar o valor do saldo e registrar mudança no banco de dados  

---
<br>
<br>



## A classe banco de dados deve fazer:

**cadastro:**  
criar tabela e guardar nome, cpf, numero, email e idade do usuário e senha  
cria uma tabela para o extrato do usuário  
<br>

**login:**  
receber cpf e senha e verificar os dados no banco de dados  
retornar true ou false se existir ou não  
<br>

**depósito:**  
receber valor do depósito e nome do usuário e atualizar na tabela dele  
adicionar a operação realizada na tabela do extrato  
<br>

**saque:**  
receber valor do saque e nome do usuário e atualizar na tabela dele  
adicionar a operação realizada na tabela do extarto  
<br>

**extrato:**  
retorna todos as operações da tabela extrato  
<br>
<br>

## Fluxograma de casos de uso:
![Fluxograma](https://github.com/osmozeInc/projeto-conta-bancaria/assets/168863507/32c839cd-bf58-4b70-9445-b0c094c480b0)
