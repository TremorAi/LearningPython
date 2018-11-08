__author__ = "Tremor"
import sqlite3

class NlpDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(r'D:\Python\twitch projects\learn_programming\async_twitch_bot\nlp.db')
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE if not exists noun
        (word text)''')
        cursor.execute('''CREATE TABLE if not exists verb
        (word text)''')
        cursor.execute('''CREATE TABLE if not exists adjective
        (word text)''')
        self.conn.commit()
        cursor.close()

    def add_noun(self, word):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO noun (word) VALUES (?)", (word,))
        self.conn.commit()
        cursor.close()


    def get_noun(self, word):
        cursor = self.conn.cursor()
        return cursor.execute('select word from noun where word =?', (word,)).fetchone()[0]

    def exists_noun(self, word):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM noun WHERE word = ? LIMIT 1)', (word,)).fetchone()[0])

    def add_verb(self, word):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO verb (word) VALUES (?)", (word,))
        self.conn.commit()
        cursor.close()

    def get_verb(self, word):
        cursor = self.conn.cursor()
        return cursor.execute('select word from verb where word =?', (word,)).fetchone()[0]

    def exists_verb(self, word):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM verb WHERE word = ? LIMIT 1)', (word,)).fetchone()[0])

    def add_adjective(self, word):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO adjective (word) VALUES (?)", (word,))
        self.conn.commit()
        cursor.close()

    def get_adjective(self, word):
        cursor = self.conn.cursor()
        return cursor.execute('select word from adjective where word =?', (word,)).fetchone()[0]

    def exists_adjective(self, word):
        cursor = self.conn.cursor()
        return bool(cursor.execute('SELECT EXISTS(SELECT 1 FROM adjective WHERE word = ? LIMIT 1)', (word,)).fetchone()[0])

nlp_db = NlpDatabase()

