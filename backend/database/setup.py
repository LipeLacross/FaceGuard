import sqlite3

def create_database():
    conn = sqlite3.connect('backend/database/users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL,
                        photo_path TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Banco de dados criado com sucesso!")
