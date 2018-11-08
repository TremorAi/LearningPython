__author__ = "Tremor"

def thing1(string, number):
    if number >= 10:
        return
    print(string * number)
    thing1("*", number + 1)
thing1("*",1)   