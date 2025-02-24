import sqlite3  # Importando o módulo sqlite3

conexao = sqlite3.connect('conectar')
cursor = conexao.cursor() # Criando um cursor

#Alterar nome da tabela
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario') # Renomeando a tabela
#cursor.execute('ALTER TABLE usuarios ADD COLUNM telefone INT') # Adicionando uma coluna
cursor.execute('ALTER TABLE usuarios RENAME COLUMN COLUNM TO telefone') # Deletando uma coluna

conexao.commit() # Salvando as alterações
conexao.close() # Fechando a conexão

print('Conexão realizada com sucesso!')