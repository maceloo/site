import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Dados de exemplo para inserção
dados_produtos = [
    ('Papaína', 'B26/AUG/2023', '2025-07-25', 'ELIAH', 'APROVADO', 2851),
    ('Papaína', 'P2401098', '2026-12-01', 'SM EMPREENDIMENTO','APROVADO', 0),
    ('Papaína', 'P2405022', '2027-04-30', 'SM EMPREENDIMENTO', 'APROVADO', 0)
]

# Inserir dados na tabela produtos
cursor.executemany('''
INSERT INTO produtos (nome, lote, validade, fabricante, status_quarentena, quantidade)
VALUES (?, ?, ?, ?, ?, ?)
''', dados_produtos)

# Confirmar a transação e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
