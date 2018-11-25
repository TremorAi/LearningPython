__author__ = "Tremor"
from utility.register import commands, register
import random
from database import database, nlp
from server import pyserver

coin = ["heads", "tails"]
eightball_list = [ "LUL","It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful." ]
project = "Twitch Bot"
admin_list = ["tremorai", "userman2"]

@register("coin", False, "!coin is a command to flip a coin. Usage: !coin")
async def command_coin(bot, msg):
    bot.send_message(random.choice(coin))

@register("setproject", True, "!setproject is a admin only command to set the current project. Use !project to display the project.")
async def command_setproject(bot, msg):
    if msg.user == "tremorai":
        global project
        project = ' '.join(msg.args)
        bot.send_message(f"The project is set to: {project}")
    else:
        bot.send_message(f"You do not have the permissions to use this command.")

@register("project", False, "!project displays the current project. Usage: !project")
async def command_project(bot, msg):
    global project
    bot.send_message(f"{project}")

# def command_time(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, strftime(self.time_format))

# def command_uptime(self, c, nick, arguments_after_command, cmd):
#     self.sendmessage(c, str(datetime.strptime(strftime(self.time_format), self.time_format) - str(datetime.strptime(arguments_after_command, self.time_format))))

@register("8ball", False, "!ball is used to display a 8ball message. usage:!8ball string")
async def command_8ball(bot,msg):
    bot.send_message(random.choice(eightball_list))

@register("attractive?", False, "The !attractive? command tells you how good looking you are /10. usage: !atractive?")
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
@register("amount", False, "!amount is used to show your tbucks amount from the database. Usage: !tbucks")
async def command_ammount(bot, msg):
    if msg.user in database.db:
        bot.send_message(f"{msg.user} has {database.db.check_balance(msg.user)} tbucks")
    else:
        bot.send_message(f"{msg.user} is not registered in the database.db, use the !register command to register.")

@register("register", False, "!register is used to register a user into the database to earn tbucks (stream money) usage:!register")
async def command_register(bot, msg):
    if msg.user not in database.db:
        database.db.add_user(msg.user)
        bot.send_message(f"{msg.user} has been added to the database")
    else:
        bot.send_message(f"{msg.user} already exists in the database.")

@register("addcmd", False, "!addcmd is used to add a command to the bot (command just sends string when called) usage:!addcmd commandname string")
async def command_addcmd(bot, msg):
    if not msg.args:
        bot.send_message("No command input: usage !addcmd args")
        return
    if not database.db.command_exists(msg.args[0]) and not msg.args[0] in commands:
        database.db.add_command("".join(msg.args[0]), " ".join(msg.args[1:]))
        bot.send_message(f"{msg.args[0]} was added!")
    else:
        bot.send_message(f"{msg.args[0]} already exists! try !{msg.args[0]}")

@register("delcmd", False, "!delcmd is used to delte a user added command to the database usage: !delcmd commandname")
async def command_delcmd(bot, msg):
    if database.db.command_exists(msg.args[0]):
        database.db.del_command(msg.args[0])
        bot.send_message(f"{msg.args[0]} has been deleted!")
    else:
        bot.send_message(f"{msg.args[0]} does not exist try adding it using !addcmd args")

@register("ask", False, "")
async def command_ask(bot,msg):
    question = ' '.join(msg.args)
    bot.send_message(f"{nlp.respond_to(question)}")

@register("welcome", False, "")
async def command_welcome(bot,msg):
    bot.send_message(f"Welcome to the Tremorai live stream")

@register("gamble", False, "!gamble command is for betting mooney. Usage: !gamble amount heads/tails")
async def command_bet(bot,msg):
    amount = msg.args[0]
    pcoin = msg.args[1]

    if msg.user not in database.db:    
        bot.send_message(f"{msg.user} is not inside the database use !register to join.")
        return

    if random.choice(coin) == pcoin:
        database.db.add_user_tbucks(msg.user, amount)
        bot.send_message(f"{msg.user} won and now has {database.db.check_balance(msg.user)} tbucks")
    else:
        database.db.subtract_tbucks(msg.user, amount)
        bot.send_message(f"{msg.user} lost and now has {database.db.check_balance(msg.user)} tbucks")

@register("give", True, "This is a admin command to give players tbucks. Usage: !give playername amount")
async def command_give(bot,msg):
    if msg.user not in admin_list:
        bot.send_message(f"{msg.user} does not have the permissions to use this command. (good try theif)")
        return
    
    playername = msg.args[0]
    amount = msg.args[1]

    if playername in database.db:
        database.db.add_user_tbucks(playername, amount)
        bot.send_message(f"{msg.user} has given {playername} {amount} tbucks! (what a scandal..)")
    else:
        bot.send_message(f"{playername} does not exist in database.db have them use !register")

@register("take", False, "This is a admin only command to take tbucks. Usage: !take playername amount")   
async def command_take(bot,msg):
    if msg.user not in admin_list:
        bot.send_message(f"{msg.user} does not have the permissions to use this command. (good try theif)")
        return

    playername = msg.args[0]
    amount = msg.args[1]
    if playername in database.db:
        database.db.subtract_tbucks(playername, amount)
        bot.send_message(f"{msg.user} has taken {amount} tbucks from {playername} (oh no!)")
    else:
        bot.send_message(f"{playername} does not exist in database.db have them use !register")

@register("weapon", False, "!weapon is used to display the current weapon you own (default is wood sword) usage: !weapon")
async def command_weapon(bot,msg):
    if msg.user in database.db:
        bot.send_message(f"{msg.user} has a {database.db.check_weapon(msg.user)} ")
    else:
        bot.send_message(f"{msg.user} is not registered in the database.db, use the !create command to register.")

    
@register("buy", False, "")
async def command_buy(bot,msg):
    if msg.args:
        weaponname = " ".join(msg.args)            
    else:
        bot.send_message(f"steel sword: 100tbucks, slime sword: 200tbucks, mace: 400tbucks, sword fish: 800tbucks, admin sword: 100000000000tbucks")
        return
    if msg.user not in database.db:
        bot.send_message(f"{msg.user} is not in the database.db use !register to join the database.db")
        return
    if database.db.check_user_weapon(msg.user) == weaponname:
        bot.send_message(f"{msg.user} already has {weaponname}")
        return

    if database.db.check_weapon(weaponname) != True:
        bot.send_message(f"{weaponname} does not exist inside the database.db")
        return
    
    if int(database.db.check_balance(msg.user)) >= database.db.get_weapon_cost(weaponname):
        database.db.subtract_tbucks(msg.user, database.db.get_weapon_cost(weaponname))
        database.db.add_user_weapon(msg.user, weaponname, database.db.get_weapon_damage(weaponname))
        bot.send_message(f"{msg.user} has bought {weaponname} for {database.db.get_weapon_cost(weaponname)} tbucks!")
    else:
        bot.send_message(f"{msg.user} needs {database.db.get_weapon_cost(weaponname) - int(database.db.check_balance(msg.user))} more tbucks.")

@register("boss", False, "!boss command is used to display the boss hp or to attack the boss. usage: !boss, !boss fight")
async def command_boss(bot,msg):
    if msg.args:
        fight = msg.args[0]
    else:
        bot.send_message(f"the boss has {database.db.get_boss_hp()} health.")
        return

    if fight != "fight":
        bot.send_message(f"{fight} is not a valid command for !boss, usage: !boss, !boss fight")
        return
    
    database.db.subtract_boss_health(database.db.get_user_weapon_damage(msg.user))
    database.db.add_damage_dealt(msg.user, database.db.get_user_weapon_damage(msg.user))
    bot.send_message(f"{msg.user} hit the boss for {database.db.get_user_weapon_damage(msg.user)} damage! The boss now has {database.db.get_boss_hp()} health.")

    if database.db.get_boss_hp() <= 0:
        await bot.send_message("defeated")
        bot.send_message(f"{msg.user} dealt the final blow against the boss!")
        database.db.set_boss_health(100000)
        user_list = database.db.get_all_users()
        for (user,) in user_list:
            if database.db.get_damage_dealt(user) > 0:
                database.db.add_user_tbucks(user, database.db.get_damage_dealt(user))
                bot.send_message(f"{user} dealt {database.db.get_damage_dealt(user)} damage and thus gained that many tbucks!")
                database.db.reset_damage_dealt(user, 0)

@register("overlay", False, "")
async def command_overlay(bot,msg):
    if msg.args:
        await bot.send_message(msg.args[0])
    else:
        await bot.send_message("test")
            
    

    



