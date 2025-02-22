import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('teste')
cursor = conexao.cursor() # Criando um cursor

# Alterar nome da tabela
# cursor.execute('ALTER TABLE usuarios RENAME TO usuario') # Renomeando a tabela
# cursor.execute('ALTER TABLE usuario ADD COLUNM telefone INT') # Adicionando uma coluna
# cursor.execute('ALTER TABLE usuario DROP COLUMN telefone') # Deletando uma coluna
cursor.execute('ALTER TABLE usuario RENAME COLUMN COLUNM TO telefone_contato') # Renomeando uma coluna

conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')