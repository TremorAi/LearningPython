__author__ = "Tremor"

commands = {}

class Command:
    def __init__(self, name, mod_only, helpmsg, func):
        self.name = name
        self.mod_only = mod_only
        self.func = func
        self.helpmsg = helpmsg

def register(name, mod_only, helpmsg):
    def inner(func):
        command = Command(name, mod_only, helpmsg, func)
        commands[name] = command
        return command
    return inner

async def command_notfound(bot, _): 
    bot.send_message('Command not found!')

notfound = Command(None, False, None,  command_notfound)