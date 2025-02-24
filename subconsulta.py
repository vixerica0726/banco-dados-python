import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('conectar.db')
cursor = conexao.cursor()

# Verificar se a tabela 'usuarios' existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Se a tabela 'usuarios' não existir, criá-la
if 'usuarios' not in [tabela[0] for tabela in tabelas]:
    cursor.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT
        );
    ''')

# Se a tabela 'gerentes' não existir, criá-la
if 'gerentes' not in [tabela[0] for tabela in tabelas]:
    cursor.execute('''
        CREATE TABLE gerentes (
            id INTEGER PRIMARY KEY,
            nome_gerente TEXT
        );
    ''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Maria')")
cursor.execute("INSERT INTO gerentes (nome_gerente) VALUES ('Carlos')")
cursor.execute("INSERT INTO gerentes (nome_gerente) VALUES ('Ana')")

# Salvar os dados
conexao.commit()

# Subconsulta Simples: Encontrar o nome do gerente de João
print("Subconsulta Simples:")
cursor.execute('''
    SELECT nome_gerente
    FROM gerentes
    WHERE id = (SELECT id FROM usuarios WHERE nome = 'João')
''')
for linha in cursor.fetchall():
    print(linha)

# Subconsulta com Múltiplas Linhas: Encontrar os usuários que têm o gerente 'Carlos'
print("\nSubconsulta com Múltiplas Linhas:")
cursor.execute('''
    SELECT nome
    FROM usuarios
    WHERE id IN (SELECT id FROM gerentes WHERE nome_gerente = 'Carlos')
''')
for linha in cursor.fetchall():
    print(linha)

# Fechar a conexão
conexao.close()
