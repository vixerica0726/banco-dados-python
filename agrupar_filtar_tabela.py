import sqlite3  # Importando o módulo sqlite3

# Conectando ao banco de dados (arquivo .db)
conexao = sqlite3.connect('conectar')
cursor = conexao.cursor()  # Criando um cursor


dados= cursor.execute('SELECT nome FROM usuarios GROUP BY nome')
for usuarios in dados:
    print(usuarios) 

dados= cursor.execute('SELECT nome FROM usuarios GROUP BY nome HAVING id>5')
for usuarios in dados:
    print(usuarios) 


# Salvando as alterações
conexao.commit()
conexao.close()  # Fechando a conexão

print('Registro atualizado com sucesso!')