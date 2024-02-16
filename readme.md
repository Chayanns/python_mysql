# Conexão do Python com o MySql

!["Imagem Python com MySQL"](image.png)

## Drive de comunicação
Para estabelecer a comunicação entre o Python e o banco de dados mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#description"> https://pypi.org/project/mysql-connector-python/#description</a>

### Comando para instalar o drive 
``` python
     python -m pip install mysql-connector-python
```

### Configuração do banco de dados MySQL
O nosso banco de dados está em um container de docker. Para acessá-lo será necessário criar o container, então faremos os seguintes comandos em um servidor Fedora com o docker instalado:

### Criação do volume 
```shell
mkdir dadosclientes
```

### Criação do container
<center>
<img src="image-2.png" height="100" width="100"></center>

```shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql 
```

### Criação do banco de dados e da tabela clientes 
```
CREATE DATABASE banco;
USE banco;
CREATE TABLE clientes(
clientes_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)
```


```Python
# Importando a a biblioteca de conexão com o banco
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
    password="SENAC@123",
    database="banco"
)    
 # Estamos c
print(conexao)
 
#para se movimentar dentro da estrutura de
# banco de dados e retornar dos dados necessário
# iremos criar um cursor
cursor = conexao.cursor()
 
# Vamos executar um comando usando  o cursor
cursor.execute("Create database Ola")
 
# vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")
 
# Vamos selecionar todos os bancos de dados na tabela cliente
cursor.execute("Insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@oul.com.br','(11)95487-6512')")
print(cursor)
for c in cursor:
    print(f"Id do cliente: {c [0]}")
    print(f"Nome do cliente: {c [1]}")
    print(f"Email: {c [2]}")
 
```
### Arquivo de cadastro: cad_clientes.py

```python
 import mysql.connector as mc

# Estabelecer uma conexão com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# verificar se a conexão foi estabelecida
print(cx)

# Criação de variavéi para o usuário passar para os dados do clientes
# para cadastrar

nome = input("Digite o nome do cliente:")
email = input("Digite o email do cliente:")
telefone = input("Digite o telefone do cliente:")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# confirmar a inserção dos dados na tabela
cx.commit()

```
### Arquivo de atualização: up_clientes.py
```python
import mysql.connector as mc
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print (i)

print("O que você deseja atualizar, digite:")
print("1 - para Nome")
print("2 - para E-mail")
print("3- para Telefone") 
op = input("Digite a opção desejada: ")
id = input("Agora, digite o id do cliente: ") 
dado = input("Digite a nova informação: ")
if(op=="1"):
   cursor.execute("update clientes set nome_cliente='"+dado+"'where clientes_id="+id) 
elif(op=="2"):
    cursor.execute("update clientes set email='"+dado+"'where clientes_id="+id)
elif(op=="3"):
    cursor.execute("update clientes set telefone='"+dado+"'where clientes_id="+id)        
else:
    print("Opção inválida!")
    
cx.commit()
```

### Criação do arquivo del_clientes.py
```python
import mysql.connector as mc
import os

con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)    

os.system("cls")

cursor = con.cursor()
cursor.execute("Select * from clientes")
for c in cursor:
    print(c) 

id = input("Digite o id do cliente que deseja apagar: ")
rs = input("Você realmente deseja apagar este cliente. Digite (s ou n): ")
if(rs=="s" or rs=="S"):
    cursor.execute(" delete from clientes where clientes_id="+id)
    con.commit()
else:
    print("------------------Opção inválida--------------------------")   

 ```