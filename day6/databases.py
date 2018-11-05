import dataset 
import sqlite3
nick = "Tremorai3"
password = "test"
islame= "NO"
test = "hsdahfsda"

def db1():
    db = dataset.connect('sqlite:///THANG.db')

    table = db['sometable']
    table.insert(dict(name='john doe' , age= 37))
    table.insert(dict(name='Jane Doe', age=34, gender='female'))

    john = table.find_one(name='johndoe')

def db2():
    conn = sqlite3.connect('THANG2.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE if not exists users
    (username text, password text, islame text)''')

    c.execute("INSERT INTO users  (username, password, islame) VALUES (?, ?, ?)", (nick, password, islame))
    res = tuple(c.execute('select 1 from users where username=?', (test,)))
    
    if res:
        print(res)
        print("??")

    

    conn.commit()
    conn.close()
db2()



