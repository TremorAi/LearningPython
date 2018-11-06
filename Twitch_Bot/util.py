__author__ = "Tremor"

import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler

def add_user_todb(db, cursor, nick):
    cursor.execute('''CREATE TABLE if not exists users
    (username text, tbucks text)''')


    res = user_in_db(cursor, nick)

    if not res:
        cursor.execute("INSERT INTO users  (username, tbucks) VALUES (?, ?)", (nick, 0))
        db.commit()
        
def add_user_tbucks(db, cursor, nick):
        return

def user_in_db(cursor, nick):
        return cursor.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username = ? LIMIT 1)', (nick,)).fetchone()[0]

def tbucks_scheduler():
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET tbucks = tbucks + 1")
        conn.commit()
        conn.close

        
        
        
   
