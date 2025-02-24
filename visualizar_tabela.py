import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

visualizar = cursor.execute('SELECT * FROM usuarios')
for usuarios in visualizar:
    print(usuarios)



conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')