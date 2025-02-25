import sqlite3  # Importando o módulo sqlite3

# Conectando ao banco de dados (arquivo .db)
conexao = sqlite3.connect('conectar')
cursor = conexao.cursor()  # Criando um cursor

dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome')
for usuarios in dados: 
    print(usuarios)
print('-------------------')

# LIMIT restringe o número de linhas retornadas.
dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome ASC LIMIT 3;')
dados = cursor.execute('SELECT * FROM usuarios LIMIT 3;')
for usuarios in dados: 
    print(usuarios)

print('-------------------')

# DISTINCT remove valores repetido
dados = cursor.execute('SELECT DISTINCT endereco FROM usuarios;')
for usuarios in dados: 
    print(usuarios)



# Salvando as alterações
conexao.commit()
conexao.close()  # Fechando a conexão

print('Registro atualizado com sucesso!')