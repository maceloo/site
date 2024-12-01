import sqlite3

# Conectar ao banco de dados (criará o arquivo estoque.db se não existir)
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Criar a tabela produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    lote TEXT,
    validade TEXT,
    fabricante TEXT,
    status_quarentena TEXT,
    quantidade INTEGER
)
''')

# Confirmar a transação e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela criados com sucesso!")
