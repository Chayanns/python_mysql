# Importando a abiblioteca de conexão com o banco 
# de dados mysql

# Vamos adicionar um alias a biblioteca

import mysql.connector as mc

# Vamos estabelecer a conexao com o banco 
# de dados e para tal, iremos passar os seguintes dados:
# servidor, porta, usuário, senha, banco 

conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)    
# Estamos testando a conexão, pedindo para 
# exibir o id da conexão. Caso exiba uma
# pilha de erros, então você tem um erro
# na linha de conexão
print(conexao)

# para se movimentar dentro da estrutura de 
# banco de dados e retornar dos dados necessários
# iremos criar um cursor
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor 
# cursor.execute("Create database Ola")
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda', 'amanda@uol.com','(11)87459-9632')")
# Vamos selecionar todos os dados da tabela cliente
cursor.execute("Select * from banco.clientes where clientes_id=1")
print(cursor)
for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"Nome do Cliente: {c[1]}")
    print(f"E-mail: {c[2]}")
          
           