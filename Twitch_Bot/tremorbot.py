__author__ = "Tremor"

import socket
import irc.bot
import config
from datetime import datetime
from time import strftime
import random
import requests

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, password, channel):

        #setup of all variables used
        self.username = username
        self.password = password
        self.channel = channel
        self.project = "Twitch bot"
        self.time_format = "%H:%M:%S"
        self.admins_and_mods = ["tremorai", "userman2", "tremorbot"]
        self.eightball_list = [ "LUL","It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful." ]
        
        #command dict
        self.commands = {
            "github":self.bot_command("https://github.com/TremorAi/LearningPython", "github"),
            "discord":self.bot_command("https://discord.gg/UU3v4Ra", "discord"),
            "language":self.bot_command("The current language is python!", "language"),
            "project":self.bot_command(None, "project"),
            "setproject":self.admin_command(None, "setproject"),
            "time":self.bot_command(None, "time"),
            "uptime":self.bot_command(strftime(self.time_format), "uptime"),
            "8ball":self.bot_command(None, "8ball"),
            

            }
       
       #Setup and use of variables to connect the bot
        host = "irc.chat.twitch.tv"
        port = 6667
        token = config.password
        username = config.username
        irc.bot.SingleServerIRCBot.__init__(self ,[(host, port, 'oauth:'+token)], self.username, self.username)

    # The on_welcome function is ran for the bot to connect to the channel that it will be chatting in
    def on_welcome(self, c, e):
        c.join(self.channel)
        print(f"joining {self.channel} ...")

    # no_permission is simply a function to send a message to the chat if the user doesnt have permission to use a command, letting them know that they don't
    def no_permission(self, nick, cmd, c):
        c.privmsg(self.channel, f"{nick} this user doesnt have the permission to use {cmd}")

    # notfound is the function ran when a command is not found inside the dict
    def notfound(self):
        def command(c, _, whatever):
            self.sendmessage(c, "command not found.")
        return command

    # This function sends a message the channel with a string whenever its called        
    def sendmessage(self, c, saystring):
        c.privmsg(self.channel, saystring)

    # bot_command is ran from the dict with instructions on what to do with the cmd 
    def bot_command(self, stringthing, cmd):
        def command(c, nick, args):

            if cmd == "project":
                self.sendmessage(c, self.project)

            elif cmd == "time":
                self.sendmessage(c, strftime(self.time_format))

            elif cmd == "uptime":
                self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - datetime.strptime(stringthing, self.time_format)))

            elif cmd == "8ball":
                self.sendmessage(c, random.choice(self.eightball_list))

            elif stringthing != None:
                self.sendmessage(c, stringthing)

        return command

    # admin_command is ran from the dict for admin commands, it checks to make sure the user is a admin (by using a list) than uses the instruction to do a command    
    def admin_command(self, stringthing, cmd):
        def command(c, nick, args):
            if nick in self.admins_and_mods:
                if cmd == "setproject":
                    self.project = args[0][len(cmd)+1:]
                    self.sendmessage(c, f"The project is set to: {self.project}")
                    print(self.project)
        return command

    # on_pubmsg checks the channel chat to see if the first letter is ! and if it is, the command is passed through do_command            
    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print('Received command: ' + cmd)
            self.do_command(e, cmd)
        return

    # do_command takes the command passed from on_pubmsg and checks to see if it is in the dict, if so passes c, nick, e.arguments to it, if not they get passed to notfound
    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        self.commands.get(cmd, self.notfound())(c, nick, e.arguments)

def main():
    channel = config.channel
    username = config.username
    password = config.password

    bot = TwitchBot(username, password, channel)
    bot.start()       
        
if __name__ == "__main__":
    main()
