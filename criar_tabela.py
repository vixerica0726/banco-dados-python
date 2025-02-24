# Teste conectando banco de dados com python.

import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

cursor.execute('CREATE TABLE usuario(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100)); ')


conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')