# Teste conectando banco de dados com python.

import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('teste')
cursor = conexao.cursor() # Criando um cursor

cursor.execute('')

conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')