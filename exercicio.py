import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor()  # Criando um cursor

# 1. Criar a tabela chamada "alunos" com os campos: id, nome, idade e curso.
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    curso TEXT NOT NULL
)
""")

# 2. Inserir 5 registros de alunos na tabela "alunos"
usuarios = [
    ("Nathan Felix", 23, "Engenharia de Software"),
    ("David Pin", 25, "Marketing"),
    ("Erica Oliveira", 19, "Análise de dados"),
    ("Martha Souza", 36, "Enfermagem"),
    ("Clarice Santos", 22, "Administração"),
    ("Allan", 31, "Mecânica")
]

# Inserir os dados na tabela 'alunos'
cursor.executemany('INSERT INTO alunos(nome, idade, curso) VALUES (?, ?, ?)', usuarios)

# 3. Consultas Básicas
# a) Mostrar todos os alunos
print("Todos os alunos:")
visualizar = cursor.execute('SELECT * FROM alunos')
for aluno in visualizar:
    print(aluno)

# b) Alunos com mais de 20 anos
print("\nAlunos com mais de 20 anos:")
maiorIdade = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in maiorIdade:
    print(aluno)

print('\nAlunos engenharia') 
curso = cursor.execute('SELECT * FROM alunos WHERE curso LIKE '%Engenharia%' ORDER BY nome;')   
for aluno in curso:
    print(aluno)


print('\n Número total de alunos')
total = cursor.execute('SELECT COUNT(*) FROM alunos;')
total_alunos = total.fetchone()[0]  # Obtendo o resultado da contagem
print(f"Total de alunos: {total_alunos}")


# Atualizando o nome do usuário com id = 1
novo_nome = "Novo Nome"
cursor.execute('UPDATE alunos SET nome = "Fabio"  WHERE nome = "Allan"')


cursor.execute('DELETE FROM usuarios where id=1')


# 1. Criar a tabela chamada "clientes" com os campos: id, nome, idade e saldo
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    saldo FLOAT NOT NULL
)
""")

# 2. Inserir alguns registros de clientes na tabela "clientes"
clientes = [
    ("Lucas Silva", 30, 5000.75),
    ("Maria Oliveira", 45, 3500.50),
    ("José Santos", 29, 1500.20),
    ("Ana Costa", 55, 10000.00),
    ("Paulo Almeida", 40, 2200.10)
]
print('Tabela "clientes" criada e dados inseridos com sucesso!')

# a) Selecionar o nome e a idade dos clientes com idade superior a 30 anos
print("a) Clientes com idade superior a 30 anos:")
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for cliente in cursor.fetchall():
    print(cliente)

# b) Calcular o saldo médio dos clientes
print("\nb) Saldo médio dos clientes:")
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]  # Pegando o resultado da média
print(f"Saldo médio: {saldo_medio:.2f}")

# c) Encontrar o cliente com o saldo máximo
print("\nc) Cliente com o saldo máximo:")
cursor.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
cliente_max_saldo = cursor.fetchone()
print(cliente_max_saldo)

# d) Contar quantos clientes têm saldo acima de 1000
print("\nd) Número de clientes com saldo acima de 1000:")
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
num_clientes = cursor.fetchone()[0]  # Pegando o número de clientes
print(f"Total de clientes com saldo acima de 1000: {num_clientes}")

# a) Atualizar o saldo de um cliente específico
id_cliente = 3  # ID do cliente para o qual vamos atualizar o saldo
novo_saldo = 3000.00  # Novo valor do saldo

cursor.execute('UPDATE clientes SET saldo = ? WHERE id = ?', (novo_saldo, id_cliente))

# b) Remover um cliente pelo seu ID
id_cliente_remover = 2  # ID do cliente a ser removido

cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente_remover,))


# 1. Criar a tabela "compras"
cursor.execute("""
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")

# 2. Inserir algumas compras associadas a clientes existentes
compras = [
    (1, "Notebook", 2500.50),
    (2, "Smartphone", 1500.30),
    (3, "Tablet", 1200.75),
    (4, "Cadeira Gamer", 850.99),
    (5, "Relógio", 300.00),
]

# Inserir os dados na tabela "compras"
cursor.executemany('INSERT INTO compras(cliente_id, produto, valor) VALUES (?, ?, ?)', compras)

# 3. Realizar a junção de tabelas para exibir o nome do cliente, produto e valor da compra
print("Consulta: Nome do Cliente, Produto e Valor da Compra")
cursor.execute("""
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
""")
for resultado in cursor.fetchall():
    print(resultado)

    
conexao.commit()  # Salvando as alterações
conexao.close()  # Fechando a conexão

print('Conexão realizada com sucesso!')
