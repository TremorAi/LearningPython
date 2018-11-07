__author__ = "Tremor"

commands = {}

class Command:
    def __init__(self, name, func):
        self.name = name
        self.func = func

def register(cmd):
    def takefunc(func):
        varthing = Command(cmd, func)
        commands[cmd] = varthing
        return varthing
    
    return takefunc

@register("Print")
def command_print():
    print("????")

print(command_print.name)
commands["Print"].func()