# Teste conectando banco de dados com python.

import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (1, "nathan", "Rua t", "erica@gmail.com", 2799336944)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (4, "davi", "Rua l", "ica@gmail.com", 27474524852)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (3, "Eric", "Rua e", "er@gmail.com", 279934545414)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (7, "allan", "Rua r", "eri@gmail.com", 254416565)')




conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')