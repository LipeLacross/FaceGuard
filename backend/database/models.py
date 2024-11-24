import sqlite3

DATABASE = 'backend/database/users.db'

def get_user_data(user_id):
    """
    Retorna os dados do usuário do banco de dados usando o ID fornecido.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        return {
            "id": user_data[0],
            "name": user_data[1],
            "address": user_data[2],
            "photo_path": user_data[3]
        }
    return {}
