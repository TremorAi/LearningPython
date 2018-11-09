__author__ = "Tremor"
from register import *
import random
from database import db
from nlp import nlp


coin = ["Heads", "Tails", "The side"]
eightball_list = [ "LUL","It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful." ]
project = "Twitch Bot"


@register("coin", False, "")
async def command_coin(bot, msg):
    bot.send_message(random.choice(coin))

@register("setproject", True, "")
async def command_setproject(bot, msg):
    global project
    print(msg.args)
    project = ' '.join(msg.args)
    bot.send_message(f"The project is set to: {project}")

@register("project", False, "")
async def command_project(bot, msg):
    global project
    bot.send_message(f"{project}")

# def command_time(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, strftime(self.time_format))

# def command_uptime(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - str(datetime.strptime(arguments_after_command, self.time_format))))

@register("8ball", False, "")
async def command_8ball(bot,msg):
    bot.send_message(random.choice(eightball_list))

@register("attractive?", False, "The !attractive? command tells you how good looking you are /10")
async def command_attractive(bot, msg):
    bot.send_message(f"You are a {str(random.randint(10,10))}/10")

@register("help", False, "The !help command will display all the commands when used without args or it will display the help msg for the command in args.")
async def command_help(bot, msg):
    commandnames = ""
    if msg.args and msg.args[0] in commands:
        bot.send_message(commands[msg.args[0]].helpmsg)
    else:
        for key in commands:
            commandnames += f"{key}, "  
        bot.send_message(commandnames[:-2])

@register("github", False, "The !github command is used for getting the github link.")
async def command_github(bot, msg):
    bot.send_message("https://github.com/TremorAi/LearningPython")

@register("discord", False, "The !discord command is used to get the discord link.")
async def command_discord(bot, msg):
    bot.send_message("https://discord.gg/UU3v4Ra")

@register("language", False, "The !language command is used to display a message with the current programming language.")
async def command_language(bot, msg):
    bot.send_message("The current language is python!")

@register("roll", False, "The command !roll rolls a dice and spits out what side it lands on.")
async def command_roll(bot, msg):
    bot.send_message(f"{msg.user} rolled a {random.randint(1,6)}")

# def command_experience(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, "My experience before the stream, ")

# def command_poll():
#         """poll will have create/stop/vote/status as the first args
#         create pollname|choice1|choice2|choice3
#         vote choice1|choice2|choice3
#         """

# def command_nerfjim():
#         return 
@register("amount", False, "")
async def command_ammount(bot, msg):
    if msg.user in db:
        bot.send_message(f"{msg.user} has {db.check_balance(msg.user)} tbucks")
    else:
        bot.send_message(f"{msg.user} is not registered in the db, use the !create command to register.")

@register("create", False, "")
async def command_create(bot, msg):
    if msg.user not in db:
        db.add_user(msg.user)
    else:
        bot.send_message(f"{msg.user} already exists in the database.")

@register("addcmd", False, "")
async def command_addcmd(bot, msg):
    if not msg.args:
        bot.send_message("No command input: usage !addcmd args")
        return
    if not db.command_exists(msg.args[0]) and not msg.args[0] in commands:
        db.add_command("".join(msg.args[0]), " ".join(msg.args[1:]))
        bot.send_message(f"{msg.args[0]} was added!")
    else:
        bot.send_message(f"{msg.args[0]} already exists! try !{msg.args[0]}")

@register("delcmd", False, "")
async def command_delcmd(bot, msg):
    if db.command_exists(msg.args[0]):
        db.del_command(msg.args[0])
        bot.send_message(f"{msg.args[0]} has been deleted!")
    else:
        bot.send_message(f"{msg.args[0]} does not exist try adding it using !addcmd args")


@register("ask", False, "")
async def command_ask(bot,msg):
    question = ' '.join(msg.args)
    bot.send_message(f"{nlp.respond_to(question)}")
    