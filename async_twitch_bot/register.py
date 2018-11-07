__author__ = "Tremor"

commands = {}

class Command:
    def __init__(self, name, mod_only, func):
        self.name = name
        self.mod_only = mod_only
        self.func = func

def register(name, mod_only):
    def inner(func):
        command = Command(name, mod_only, func)
        commands[name] = command
        return command
    return inner

