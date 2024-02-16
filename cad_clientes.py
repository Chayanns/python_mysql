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