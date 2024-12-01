import sqlite3

def remover_dados():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    
    # Exemplo: Remover todos os registros onde o nome do produto é 'Papaína'
    cursor.execute("DELETE FROM produtos WHERE nome = 'Papaína'")
    
    # Ou você pode remover registros específicos por lote
    # cursor.execute("DELETE FROM produtos WHERE lote = 'Lote 005'")
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    remover_dados()

print("Dados removidos com sucesso!")
