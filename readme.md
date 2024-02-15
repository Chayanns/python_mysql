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