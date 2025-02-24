import sqlite3  # Importando o módulo sqlite3

# Conectando ao banco de dados (arquivo .db)
conexao = sqlite3.connect('conectar')
cursor = conexao.cursor()  # Criando um cursor

# Atualizando o nome do usuário com id = 1
novo_nome = "Novo Nome"
cursor.execute('UPDATE usuarios SET endereco = "Vitoria"  WHERE nome = "allan"')

# Salvando as alterações
conexao.commit()
conexao.close()  # Fechando a conexão

print('Registro atualizado com sucesso!')
