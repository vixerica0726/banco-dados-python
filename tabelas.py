import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('conectar.db')
cursor = conexao.cursor()

# Listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas no banco de dados:")
for tabela in tabelas:
    print(tabela[0])

# Fechar a conexão
conexao.close()
import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('conectar.db')
cursor = conexao.cursor()

# Criar a tabela usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT
    );
''')

# Criar a tabela gerentes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gerentes (
        id INTEGER PRIMARY KEY,
        nome_gerente TEXT
    );
''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Maria')")
cursor.execute("INSERT INTO gerentes (nome_gerente) VALUES ('Carlos')")
cursor.execute("INSERT INTO gerentes (nome_gerente) VALUES ('Ana')")

# Commit para salvar
conexao.commit()

# Fechar a conexão
conexao.close()
