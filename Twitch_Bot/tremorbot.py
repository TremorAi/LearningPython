__author__ = "Tremor"

import socket
import irc.bot
import config
import datetime

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, password, channel):
        self.username = username
        self.password = password
        self.channel = channel
        self.project = ""
        self.admins_and_mods = ["tremorai", "userman2", "tremorbot"]
        self.commands = {
            "github":self.bot_command("https://github.com/TremorAi/LearningPython"),
            "discord":self.bot_command("https://discord.gg/UU3v4Ra"),
            "language":self.bot_command("The current language is python!"),
            "project":self.bot_command(f"{self.project}"),
            "setproject":self.bot_command(None),
            "time":self.bot_command(str(datetime.datetime.now()))

            }
        

        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        host = "irc.chat.twitch.tv"
        port = 6667
        token = config.password
        username = config.username
        irc.bot.SingleServerIRCBot.__init__(self ,[(host, port, 'oauth:'+token)], self.username, self.username)

        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket.connect((host, port))
    
    def on_welcome(self, c, e):
        c.join(self.channel)
        print(f"joining {self.channel} ...")
        # c.privmsg(self.channel,"Hello World! i work!")-

    def no_permission(self, nick, cmd, c):
        c.privmsg(self.channel, f"{nick} this user doesnt have the permission to use {cmd}")
        
    def sendmessage(self, c, saystring):
        return c.privmsg(self.channel, saystring)

    def bot_command(self, stringthing):
        def command(c, nick, args):
            if stringthing != None:
                self.sendmessage(c, stringthing)
        return command
        
    def admin_command(self, stringthing):
        def command(c, nick, args):
            if nick in self.admins_and_mods:
                if args != None:
                    pass
                

    
    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print('Received command: ' + cmd)
            self.do_command(e, cmd)
        return


    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        # if nick == "tremorbot":
        #     return

        # if cmd == "setproject":
        #     if nick == "tremorai":
        #         self.project = e.arguments[0][11:]
        #         return
        #     else:
        #         return self.no_permission(nick, cmd, c)

        self.commands.get(cmd)(c, nick, None)
                


        # if cmd == "github":
        #     self.sendmessage(c, "https://github.com/TremorAi/LearningPython")

        # elif cmd == "discord":
        #     # return c.privmsg(self.channel, "https://discord.gg/UU3v4Ra")
        #     self.sendmessage(c, "https://discord.gg/UU3v4Ra")

        # elif cmd == "language":
        #     # return c.privmsg(self.channel, f"The current language is python!")
        #     self.sendmessage(c, f"The current language is python!")

        # elif cmd == "project":
        #     # return c.privmsg(self.channel, f"{self.project}")
        #     self.sendmessage(c, f"{self.project}")

        # elif cmd == "time":
        #     self.sendmessage(c, str(datetime.datetime.now()))

        # # elif cmd == "poll":
        # #     self.poll == e.arguments[0][5:]

        # else:
        #     self.sendmessage(c, f"{e.arguments} not understood!")

def main():
    channel = config.channel
    username = config.username
    password = config.password

    bot = TwitchBot(username, password, channel)
    bot.start()       
        
if __name__ == "__main__":
    main()
