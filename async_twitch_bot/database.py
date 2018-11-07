__author__ = "Tremor"
import sqlite3
import asyncio

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('async_twitch_bot/users.db')
        cursor = self.conn.cursor()

        cursor.execute('''CREATE TABLE if not exists users
        (username text, tbucks text)''')
        self.conn.commit()
        cursor.close()
    
    def add_user(self, name, amt=0):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users  (username, tbucks) VALUES (?, ?)", (name, amt))
        self.conn.commit()
        cursor.close()

    def __contains__(self, name):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username = ? LIMIT 1)', (name,)).fetchone()[0])

    def add_tbucks(self):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET tbucks = tbucks + 1")
        self.conn.commit()
        cursor.close()

    
async def tbucks_update_loop():
    while True:
        await asyncio.sleep(3)
        db.add_tbucks()
        



db = Database()