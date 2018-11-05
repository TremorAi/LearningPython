__author__ = "Tremor"

import socket
import irc.bot
import config
from datetime import datetime
from time import strftime
import random
import requests
from commands import *

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
        self.coinflip = ["head", "tails", "THE SIDE WHAT"]

        #command dict
        self.commands = {
            "github":command_github,
            "discord":command_discord,
            "language":command_language,
            "project":command_project,
            "setproject":self.admin_command(None, "setproject"),
            "time":command_time,
            "uptime":command_uptime,
            "8ball":command_8ball,
            "attractive?":command_attractive,
            "coin":command_coin,
            "commands":command_commands,
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

    # def command_project(self, c, nick, stringthing):
    #     self.sendmessage(c, self.project)

    # def command_time(self, c, nick, stringthing):
    #     self.sendmessage(c, strftime(self.time_format))

    # def command_uptime(self, c, nick, stringthing):
    #     self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - datetime.strptime(stringthing, self.time_format)))

    # def command_8ball(self, c, nick, stringthing):
    #     self.sendmessage(c, random.choice(self.eightball_list))
    
    # def command_attractive(self, c, nick, stringthing):
    #     self.sendmessage(c, f"You are a {str(random.randint(10,10))}/10")

    # def command_coin(self, c, nick, stringthing):
    #     self.sendmessage(c, random.choice(self.coinflip))

    # def command_sendmsg(self, c, nick, stringthing):
    #     self.sendmessage(c, stringthing)

    # def command_commands(self, c, nick, stringthing):
    #     commandnames = ""
    #     for key in self.commands.keys():
    #         commandnames += f"{key}, "  
    #     self.sendmessage(c, commandnames[:-2])

    # def command_github(self, c, nick, stringthing):
    #     self.sendmessage(c, "https://github.com/TremorAi/LearningPython")

    # def command_discord(self, c, nick, stringthing):
    #     self.sendmessage(c, "https://discord.gg/UU3v4Ra")

    # def command_language(self, c, nick, stringthing):
    #     self.sendmessage(c, "The current language is python!")

    # bot_command is ran from the dict with instructions on what to do with the cmd 
    # def bot_command(self, stringthing, cmd):
    #     def command(c, nick, args):

            # if cmd == "project":
            #     self.sendmessage(c, self.project)

        #     if cmd == "time":
        #         self.sendmessage(c, strftime(self.time_format))

        #     elif cmd == "uptime":
        #         self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - datetime.strptime(stringthing, self.time_format)))

        #     elif cmd == "8ball":
        #         self.sendmessage(c, random.choice(self.eightball_list))

        #     elif cmd == "attractive?":
        #         self.sendmessage(c, f"You are a {str(random.randint(10,10))}/10")
            
        #     elif cmd == "coin":
        #         self.sendmessage(c, random.choice(self.coinflip))

        #     elif stringthing is not None:
        #         self.sendmessage(c, stringthing)

        # return command

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

        self.commands.get(cmd, self.notfound())(self, c, nick, e.arguments)

def main():
    channel = config.channel
    username = config.username
    password = config.password

    bot = TwitchBot(username, password, channel)
    bot.start()       
        
if __name__ == "__main__":
    main()
