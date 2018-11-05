__author__ = "Tremor"
from datetime import datetime
from time import strftime
import random

def command_project(self, c, nick, stringthing):
    self.sendmessage(c, self.project)

def command_time(self, c, nick, stringthing):
    self.sendmessage(c, strftime(self.time_format))

def command_uptime(self, c, nick, stringthing):
    self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - datetime.strptime(stringthing, self.time_format)))

def command_8ball(self, c, nick, stringthing):
    self.sendmessage(c, random.choice(self.eightball_list))

def command_attractive(self, c, nick, stringthing):
    self.sendmessage(c, f"You are a {str(random.randint(10,10))}/10")

def command_coin(self, c, nick, stringthing):
    self.sendmessage(c, random.choice(self.coinflip))

def command_sendmsg(self, c, nick, stringthing):
    self.sendmessage(c, stringthing)

def command_commands(self, c, nick, stringthing):
    commandnames = ""
    for key in self.commands.keys():
        commandnames += f"{key}, "  
    self.sendmessage(c, commandnames[:-2])

def command_github(self, c, nick, stringthing):
    self.sendmessage(c, "https://github.com/TremorAi/LearningPython")

def command_discord(self, c, nick, stringthing):
    self.sendmessage(c, "https://discord.gg/UU3v4Ra")

def command_language(self, c, nick, stringthing):
    self.sendmessage(c, "The current language is python!")