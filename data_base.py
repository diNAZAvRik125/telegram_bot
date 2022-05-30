import sqlite3


class dbworker:
    def __init__(self,database_file):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
           user_id INT PRIMARY KEY,
           fname TEXT,
           reason TEXT);
        """)
        self.connect.commit()
    def add_user(self, user_id, name, reason, data):
# 		'''Добавляем нового юзера'''
        self.cursor.execute("INSERT INTO user VALUES(?, ?, ?, ?);", data)
        self.connect.commit()
    def update_user_name(self, old_name, new_name):
        # обновляем имя пользвоателя
        self.cursor.execute("UPDATE users SET fname = new_name WHERE fname = old_name")
        self.connect.commit()
    def update_user_reason(self, old_reason, new_reason):
        # обновляем причину пользователя
        self.cursor.execute("UPDATE users SET reason = new_reason WHERE reason = old_reason")
        self.connect.commit()
    def delete_user(self, id):
        # удаляем пользователя
        self.cursor.execute("DELETE FROM users WHERE user_id = id;")
        self.connect.commit()

    def next_user(self, user_reason):
        for row in self.cursor.execute('SELECT * FROM users ORDER BY reason:=user_reason'):
            return row
    def get_info_user(self, user_id):
		# '''получение информации по юзеру'''
        return self.cursor.execute('SELECT * FROM users ORDER BY user_id:=user_id')


