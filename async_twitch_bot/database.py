__author__ = "Tremor"
import sqlite3
import asyncio

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(r'D:\Programming\Python\twitch projects\learn_programming\async_twitch_bot\users.db')
        # self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()

        cursor.execute('''CREATE TABLE if not exists users
        (username text, tbucks text, weapon text, damage integer, damagedealt integer)''')
        self.conn.commit()
        cursor.execute('''CREATE TABLE if not exists weapons
        (name text, damage integer, cost integer)''')
        self.conn.commit()
        cursor.execute('''CREATE TABLE if not exists commands
        (cmd text, results text)''')
        self.conn.commit()
        cursor.close()
    
    def add_user(self, name, amt=0, weapon="wood sword", damage=10, damagedealt=0):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users  (username, tbucks, weapon, damage, damagedealt) VALUES (?, ?, ?, ?, ?)", (name, amt, weapon, damage, damagedealt))
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

    def add_user_tbucks(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET tbucks = tbucks + ? WHERE username =? ", (amount, name))
        self.conn.commit()
        cursor.close()

    def add_user_weapon(self, name, weapon, dmg):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET weapon = ? WHERE username =? ", (weapon, name))
        self.conn.commit()
        cursor.execute("UPDATE users SET damage = ? WHERE username =? ", (dmg, name))
        self.conn.commit()
        cursor.close()

    def subtract_tbucks(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET tbucks = tbucks - ? WHERE username = ?",(amount, name))
        self.conn.commit()
        cursor.close()
    
    def get_weapon_cost(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select cost from weapons where name =?', (name,)).fetchone()[0]
        
    def check_balance(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select tbucks from users where username =?', (name,)).fetchone()[0]

    def check_user_weapon(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select weapon from users where username =?', (name,)).fetchone()[0]

    def check_weapon(self, name):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM weapons WHERE name = ? LIMIT 1)', (name,)).fetchone()[0])

    def add_command(self, cmd, results):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO commands (cmd, results) VALUES (?, ?)", (cmd, results))
        self.conn.commit()
        cursor.close()

    def del_command(self, cmd):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM commands where cmd =?", (cmd, ))
        self.conn.commit()
        cursor.close()

    def get_command(self, cmd):
        cursor = self.conn.cursor()
        return cursor.execute('select results from commands where cmd =?', (cmd,)).fetchone()[0]

    def get_weapon_damage(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select damage from weapons where name=?', (name,)).fetchone()[0]

    def command_exists(self, cmd):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM commands WHERE cmd = ? LIMIT 1)', (cmd,)).fetchone()[0])

    def command_name(self, name):
        pass

async def tbucks_update_loop():
    while True:
        await asyncio.sleep(3)
        db.add_tbucks()
        



db = Database()