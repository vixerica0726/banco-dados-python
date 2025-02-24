import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

cursor.execute('DELETE FROM usuarios where id=1')

conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')