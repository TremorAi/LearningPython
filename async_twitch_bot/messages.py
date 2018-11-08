__author__ = "tremor"
from fun_commands import *
from nlp import nlp

class Message:
    def __init__(self, message):
        self.user = None
        self.body = None
        self.iscommand = False
        self.command = None
        self.args = []
        self.forbidden = [":tremorai!tremorai@tremorai.tmi.twitch.tv PRIVMSG #tremorai :test", "tmi.twitch.tv 004 tremorbot :-: -", "tremorbot.tmi.twitch.tv 366 tremorbot #tremorai :End of /NAMES list: End of /NAMES list",
        ":tmi.twitch.tv 001 tremorbot :Welcome, GLHF!",
":tmi.twitch.tv 002 tremorbot :Your host is tmi.twitch.tv",
":tmi.twitch.tv 003 tremorbot :This server is rather new",
":tmi.twitch.tv 004 tremorbot :-",
":tmi.twitch.tv 375 tremorbot :-",
":tmi.twitch.tv 372 tremorbot :You are in a maze of twisty passages, all alike.",
":tmi.twitch.tv 376 tremorbot :>",
":tremorbot!tremorbot@tremorbot.tmi.twitch.tv JOIN #tremorai",
":tremorbot.tmi.twitch.tv 353 tremorbot = #tremorai :tremorbot",
":tremorbot.tmi.twitch.tv 366 tremorbot #tremorai :End of /NAMES list"]
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

        elif message not in self.forbidden:
            nlp.respond_to(self.body)
            
        # print(self.user)
        
        print(f"{self.user}: {self.body}")
def returncommand(self):
    return self.command, self.iscommand
    

# def message_command(self):
#     commands.get()()
        
   

    # :userman2 !userman2 @userman2.tmi.twitch.tv PRIVMSG #tremorai :afdfas
    # :thewastedlander !thewastedlander! @thewastedlander.tmi.twitch.tv PRIVMSG #tremorai :message yay
