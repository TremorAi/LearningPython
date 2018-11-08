__author__ = "Tremor"
import sqlite3
from nlp_database import nlp_db

import random

class Natural_language_processing:
    def __init__(self):
        pass    

    def respond_to(self, input):
        test = input.split()
        response = ""
        for i in test:
            if nlp_db.exists_noun(i):
                response += "noun" + " "
            elif nlp_db.exists_verb(i):
                response += "verb" + " "
            elif nlp_db.exists_adjective(i):
                response += "adjective" + " "
            else:
                random_index = random.randrange(len(choice))
                choice[random_index](i)
                response += name_choice[random_index] + "?" + " "
        return response


choice = [nlp_db.add_noun, nlp_db.add_verb, nlp_db.add_adjective]
name_choice = ["noun", "verb", "adjective"]

nlp = Natural_language_processing()        
# print(nlp.respond_to("cats eat mice test"))
