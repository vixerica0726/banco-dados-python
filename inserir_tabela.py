# Teste conectando banco de dados com python.

import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (1, "nathan", "Rua", "erica@gmail.com", 2799336944)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (5, "davi", "Radd", "erica@gmail.com", 2799336944)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (4, "Eric", "Rgda", "erica@gmail.com", 2799336944)')
cursor.execute('INSERT INTO usuarios(id,nome,endereco,email,telefone) VALUES (6, "allan", "Rudcfa", "erica@gmail.com", 2799336944)')




conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')