__author__ = "Tremor"

import sqlite3

def add_user_todb(self, c, db, cursor, nick):
    cursor.execute('''CREATE TABLE if not exists users
    (username text, tbucks text)''')


    res = tuple(cursor.execute('select 1 from users where username=?', (nick,)))

    if not res:
        cursor.execute("INSERT INTO users  (username, tbucks) VALUES (?, ?)", (nick, 0))
        db.commit()
        self.sendmessage(c, f"new tbucks user {nick} is now in the db ")
        
    
        
        
   
