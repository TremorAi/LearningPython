__author__ = "Tremor"
import sqlite3
import asyncio

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(r'D:\Programming\Python\twitch projects\learn_programming\async_twitch_bot\database\users.db')
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
        cursor.execute('''CREATE TABLE if not exists boss
        (name text, health integer)''')
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

    def add_damage_dealt(self, name, dmg):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET damagedealt = damagedealt + ? WHERE username =? ", (dmg, name))
        self.conn.commit()
        cursor.close()

    def reset_damage_dealt(self, name, dmg):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET damagedealt = ? WHERE username =? ", (dmg, name))
        self.conn.commit()
        cursor.close()
    
    def reset_all_tbucks(self, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET tbucks = ?", (amount,))
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

    def get_user_weapon_damage(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select damage from users where username =?', (name,)).fetchone()[0]
        
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

    #boss fight stuff
    def get_boss_hp(self):
        cursor = self.conn.cursor()
        return cursor.execute('select health from boss where name=?', ("jim",)).fetchone()[0]

    def get_player_hp(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select health from users where username=?', (name,)).fetchone()[0]
    
    def set_boss_health(self, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE boss SET health = ? WHERE name = ?",(amount, "jim"))

    def set_player_health(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET health = ? WHERE username = ?",(amount, name))
    
    def subtract_boss_health(self, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE boss SET health = health - ? WHERE name = ?",(amount, "jim"))

    def get_all_users(self):
        cursor = self.conn.cursor()
        return cursor.execute("select username from users").fetchall()
    
    def get_damage_dealt(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select damagedealt from users where username =?', (name,)).fetchone()[0]

    def get_boss_damage(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select damage from boss where name =?', (name,)).fetchone()[0]

    def subtract_player_health(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET health = health - ? WHERE username = ?",(amount, name))

    def get_player_default_hp(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select default_hp from users where username =?', (name,)).fetchone()[0]

    def add_player_default_hp(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET deafult_hp = default_hp + ? WHERE username= ?",(amount, name))

    def add_player_health(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET health = health + ? WHERE username= ?",(amount, name))

    def get_player_exp(self, name):
        cursor = self.conn.cursor()
        return cursor.execute('select experience from users where username =?', (name,)).fetchone()[0]

    def add_player_exp(self, name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET experience = experience + ? WHERE username= ?",(amount, name))

    def check_food(self, name):
            cursor = self.conn.cursor()
            return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM food WHERE name = ? LIMIT 1)', (name,)).fetchone()[0])

    def get_food_cost(self, name):
            cursor = self.conn.cursor()
            return cursor.execute('select cost from food where name =?', (name,)).fetchone()[0]

    def get_food_hp_amount(self, name):
            cursor = self.conn.cursor()
            return cursor.execute('select health from food where name =?', (name,)).fetchone()[0]



async def tbucks_update_loop():
    while True:
        await asyncio.sleep(3)
        db.add_tbucks()
        



db = Database()