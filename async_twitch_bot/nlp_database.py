__author__ = "Tremor"
import sqlite3

class NlpDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(r'D:\Python\twitch projects\learn_programming\async_twitch_bot\nlp.db')
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE if not exists noun
        (id integer primary key, word text)''')
        cursor.execute("INSERT INTO noun (word) VALUES (?), (?), (?), (?), (?), (?), (?), (?), (?), (?)", ("people","history", "way","art","world","information","map","two","family","goverment"))

        cursor.execute('''CREATE TABLE if not exists verb
        (id integer primary key, word text)''')
        cursor.execute("INSERT INTO verb (word) VALUES (?), (?), (?), (?), (?), (?), (?), (?), (?), (?)", ("be","am", "is","are","was","were","been","being","have","has"))

        cursor.execute('''CREATE TABLE if not exists adjective
        (id integer primary key, word text)''')
        cursor.execute("INSERT INTO adjective (word) VALUES (?), (?), (?), (?), (?), (?), (?), (?), (?), (?)", ("good","new", "first","last","long","great","little","own","other","old"))

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

    def get_rand_noun(self):
        cursor = self.conn.cursor()
        return cursor.execute('SELECT word FROM noun WHERE id IN (SELECT id FROM noun ORDER BY RANDOM() LIMIT 1)').fetchone()[0]

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
    
    def get_rand_verb(self):
        cursor = self.conn.cursor()
        return cursor.execute('SELECT word FROM verb WHERE id IN (SELECT id FROM verb ORDER BY RANDOM() LIMIT 1)').fetchone()[0]

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

    def get_rand_adjective(self):
        cursor = self.conn.cursor()
        return cursor.execute('SELECT word FROM adjective WHERE id IN (SELECT id FROM adjective ORDER BY RANDOM() LIMIT 1)').fetchone()[0]

    def get_rand_word(self,type):
        if type == "verb":
            return self.get_rand_verb()
        elif type == "noun":
            return self.get_rand_noun()
        elif type == "adjective":
            return self.get_rand_adjective()


nlp_db = NlpDatabase()

