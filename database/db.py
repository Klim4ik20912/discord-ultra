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
    
    def ban(self, user_id: int, admin_id: int, reason: str):
        try:
            self.cursor.execute(f"UPDATE users SET ban = {1} WHERE user = ?", (user_id))
            self.cursor.execute(f"UPDATE users SET banned_by = ? WHERE user = ?", (admin_id, user_id))
            self.connection.commit()
            return True
        except Exception as e:
            return False
        
    def get_bal(self, user_id: int) -> int:
        balance = self.cursor.execute("SELECT balance FROM users WHERE user = ?", (user_id)).fetchone()[0]
        return balance