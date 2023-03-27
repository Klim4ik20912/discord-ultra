from config import *

import sqlite3



class SQLighter:
    # При объявление класса
    def __init__(self, db):
        # Подключаемся к бд
        self.connection = sqlite3.connect("discord.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            user INT,
            balance BIGINT,
            text_stat BIGINT,
            warns INT,
            mute DATETIME,
            ban INT,
            banned_by TEXT,
            verified_by TEXT,
            voice_stat INT,
            games_count BIGINT
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS roles (
            role_id INT,
            id INT PRIMARY KEY,
            cost INT,
            owner_id INT,
            count_bought INT,
            lifetime DATETIME
        )""")

        self.connection.commit()

    def register(self, user_id: int, admin: int) -> bool:
        if self.cursor.execute(f"SELECT user FROM users WHERE user = ?", (user_id,)).fetchone() == None:
            self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, 0, 0, 0, None, 0, None, admin, 0, 0))
            self.connection.commit()
            return True
        else:
            return False
    
    def ban(self, user_id: int, admin: str, reason: str):
        try:
            self.cursor.execute(f"UPDATE users SET ban = {1} WHERE user = ?", (user_id,))
            self.cursor.execute(f"UPDATE users SET banned_by = ? WHERE user = ?", (admin, user_id,))
            self.connection.commit()
            return True
        except Exception as e:
            return False
        
    def get_bal(self, user_id: int) -> int:
        balance = self.cursor.execute(f"SELECT balance FROM users WHERE user = {user_id}").fetchone()[0]
        return balance

    def check_user(self, user_id: int) -> bool:
        if self.cursor.execute(f"SELECT * FROM users WHERE user = ?", (user_id,)).fetchone() == None:
            return False
        else:
            return True
        
    def trans(self, user: int, recipient: int, money: int) -> bool:
        try:
            self.cursor.execute(f"UPDATE users SET balance = {self.get_bal(user) - money} WHERE user = {user}")

            self.cursor.execute(f"UPDATE users SET balance = {self.get_bal(recipient) + money} WHERE user = {recipient}")
            self.connection.commit()
            return True
        except:
            return False
        
    def add_bal(self, user):
        self.cursor.execute(f"UPDATE users SET balance = {50000} WHERE user = {user}")
        self.connection.commit()
    
    def unban(self, user):
        try:
            self.cursor.execute(f"UPDATE users SET ban = {0} WHERE user = ?", (user,))
            self.cursor.execute(f"UPDATE users SET banned_by = None WHERE user = ?", (user,))
            self.connection.commit()
            return True
        except Exception as e:
            return False
    
    def append_bal(self, user: int, money: int):
        balance = self.get_bal(user)
        self.cursor.execute(f"UPDATE users SET balance = {balance + money} WHERE user = {user}")
        self.connection.commit()
        return True