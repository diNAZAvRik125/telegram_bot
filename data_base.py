import sqlite3


class DataBaseWorker:
    def __init__(self,database_file):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
           user_id INT PRIMARY KEY,
           fname TEXT,
           reason TEXT);
        """)
        self.connect.commit()
    def add_user(self, id, name, rs):
# 		'''Добавляем нового юзера'''
        self.cursor.execute("INSERT INTO `users` (`user_id`, `fname`,`reason`) VALUES(?,?,?)", (id, name, rs))
        self.connect.commit()
    def update_user_reason(self, old_reason, new_reason):
        # обновляем причину пользователя
        self.cursor.execute("UPDATE users SET reason = new_reason WHERE reason = old_reason")
        self.connect.commit()
    def delete_user(self, id):
        # удаляем пользователя
        self.cursor.execute("DELETE FROM users WHERE user_id = id;")
        self.connect.commit()

    def find_user(self, user_reason, data):
        data = self.cursor.execute('SELECT * FROM users WHERE reason = user_reason').fetchall()
        return data
    def get_info_user(self, id):
		# '''получение информации по юзеру'''
        user = self.connect.execute('SELECT * FROM users WHERE user_id = id').fetchone()
        return user[2]


