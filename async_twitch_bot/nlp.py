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
                response += f"{nlp_db.get_rand_noun()}  "
            elif nlp_db.exists_verb(i):
                response += f"{nlp_db.get_rand_verb()}  "
            elif nlp_db.exists_adjective(i):
                response += f"{nlp_db.get_rand_adjective()}  "
            else:
                # random_index = random.randrange(len(choice))
                # choice[random_index](i)
                response += nlp_db.get_rand_word(self.predictChoice(i)) + " "

                

                # print(f"Bag: {nlp_db.get_rand_verb()} {nlp_db.get_rand_noun()} {nlp_db.get_rand_adjective()} input: {i}")
        return response

    def predictChoice(self, word):
        rand_words = [nlp_db.get_rand_noun(), nlp_db.get_rand_verb(), nlp_db.get_rand_adjective()]

        noun = abs(len(word) - len(rand_words[0]))
        verb = abs(len(word) - len(rand_words[1]))
        adjective = abs(len(word) - len(rand_words[2]))

        l = [noun,verb,adjective]
        thing = l.index(min(l))

        choice[thing](word)
        return name_choice[thing]
        


choice = [nlp_db.add_noun, nlp_db.add_verb, nlp_db.add_adjective]
name_choice = ["noun", "verb", "adjective"]

nlp = Natural_language_processing()        
# print(nlp.respond_to("cats eat mice test"))
