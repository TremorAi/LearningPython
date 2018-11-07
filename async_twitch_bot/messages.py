__author__ = "tremor"
from fun_commands import *

class Message:
    def __init__(self, message):
        self.user = None
        self.body = None
        self.iscommand = False
        self.command = None
        self.args = []
        self.message_parser(message)
        
        

    def message_parser(self, message):
        new_message = message[1:]
        new_message = new_message.split("!")[0]
        self.user = new_message

        self.body = message[1:].partition(":")[-1]

        if self.body.startswith("!"):
            self.iscommand = True
            self.command = self.body[1:].split()[0]
            self.args = self.body[len(self.command)+1:].split()
            # message_command(self)
            

        print(f"{self.user}: {self.body}")
def returncommand(self):
    return self.command, self.iscommand
    

# def message_command(self):
#     commands.get()()
        
   

    # :userman2 !userman2 @userman2.tmi.twitch.tv PRIVMSG #tremorai :afdfas
    # :thewastedlander !thewastedlander! @thewastedlander.tmi.twitch.tv PRIVMSG #tremorai :message yay
