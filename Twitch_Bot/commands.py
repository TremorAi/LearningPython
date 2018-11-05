__author__ = "Tremor"
from datetime import datetime
from time import strftime
import random

def getcommands():
        #command dict
    return {
        "github":command_github,
        "discord":command_discord,
        "language":command_language,
        "project":command_project,
        "setproject":command_setproject,
        "time":command_time,
        "uptime":command_uptime,
        "8ball":command_8ball,
        "attractive?":command_attractive,
        "coin":command_coin,
        "commands":command_commands,
        "roll":command_roll,
        
        }
   

def command_setproject(self, c, nick, arguments_after_command, cmd):
    if nick in self.admins_and_mods:
        self.project = arguments_after_command[0][len(cmd)+1:]
        self.sendmessage(c, f"The project is set to: {self.project}")

def command_project(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, self.project)

def command_time(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, strftime(self.time_format))

def command_uptime(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - datetime.strptime(arguments_after_command, self.time_format)))

def command_8ball(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, random.choice(self.eightball_list))

def command_attractive(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, f"You are a {str(random.randint(10,10))}/10")

def command_coin(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, random.choice(self.coinflip))

def command_sendmsg(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, arguments_after_command)

def command_commands(self, c, nick, arguments_after_command, cmd):
    commandnames = ""
    commands = getcommands()
    for key in commands.keys():
        commandnames += f"{key}, "  
    self.sendmessage(c, commandnames[:-2])

def command_github(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, "https://github.com/TremorAi/LearningPython")

def command_discord(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, "https://discord.gg/UU3v4Ra")

def command_language(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, "The current language is python!")

def command_roll(self, c, nick, arguments_after_command, cmd):
    self.sendmessage(c, f"{nick} rolled a {random.randint(1,6)}")