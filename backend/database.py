import sqlite3

def get_db_connection():
    conn = sqlite3.connect('aromawake.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect('aromawake.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS formularios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT,
                   mensagem TEXT,
                   data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )
                   ''')
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            assunto TEXT,
            mensagem TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    conn.commit()
    conn.close()
    print("Base de dados criada com sucesso")

if __name__ == "__main__":
    init_db()