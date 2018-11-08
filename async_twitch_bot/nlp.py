__author__ = "Tremor"

import random

class Natural_language_processing:
    def __init__(self, nouns, verbs, adjectives):
        self.nouns = nouns
        self.verbs = verbs
        self.adjectives = adjectives

    def respond_to(self, input):
        test = input.split()
        for i in test:
            if i in noun:
                print("noun")
            elif i in verb:
                print("verb")
            else:
                random_index = random.randrange(len(choice))
                choice[random_index].append(i)
                print(f"{name_choice[random_index]}?")

noun = ["cats", "mice"]
verb = ["eat"]
adjective = []
choice = [noun, verb, adjective]
name_choice = ["noun", "verb", "adjective"]

nlp = Natural_language_processing(noun, verb, adjective)        
nlp.respond_to("cats eat mice test")
print("")
nlp.respond_to("cats eat mice test")      