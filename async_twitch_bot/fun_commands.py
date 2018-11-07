__author__ = "Tremor"
from register import *
import random


coin = ["Heads", "Tails", "The side"]
project = "Twitch Bot"


@register("coin", False)
async def command_coin(bot, msg):
    bot.send_message(random.choice(coin))

@register("setproject", True)
async def command_setproject(bot, msg):
    global project
    print(msg.args)
    project = ' '.join(msg.args)
    bot.send_message(f"The project is set to: {project}")

@register("project", False)
async def command_project(bot, msg):
    global project
    bot.send_message(f"{project}")

# def command_time(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, strftime(self.time_format))

# def command_uptime(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - str(datetime.strptime(arguments_after_command, self.time_format))))

# def command_8ball(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, random.choice(self.eightball_list))

# def command_attractive(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, f"You are a {str(random.randint(10,10))}/10")

# def command_coin(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, random.choice(self.coinflip))

# def command_sendmsg(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, arguments_after_command)

# def command_commands(self, c, nick, arguments_after_command, cmd):
#     commandnames = ""
#     commands = getcommands()
#     for key in commands.keys():
#         commandnames += f"{key}, "  
#     self.sendmessage(c, commandnames[:-2])

# def command_github(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, "https://github.com/TremorAi/LearningPython")

# def command_discord(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, "https://discord.gg/UU3v4Ra")

# def command_language(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, "The current language is python!")

# def command_roll(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, f"{nick} rolled a {random.randint(1,6)}")

# def command_experience(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, "My experience before the stream, ")

# def command_poll():
#         """poll will have create/stop/vote/status as the first args
#         create pollname|choice1|choice2|choice3
#         vote choice1|choice2|choice3
#         """

# def command_nerfjim():
#         return 

# def command_ammount(self, c, nick, arguments_after_command, cmd):
#     db_c = self.conn.cursor()
#     res = user_in_db(db_c, nick)

#     if  res:
#         tbucks = db_c.execute('select tbucks from users where username =?', (nick,)).fetchone()[0]
#         self.sendmessage(c, f"{nick} has {tbucks} tbucks")

# def command_create(self, c, nick, arguments_after_command, cmd):
#     db_c = self.conn.cursor()
#     add_user_todb(self.conn, db_c, nick)

