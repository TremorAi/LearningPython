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
        # c.privmsg(self.channel,"Hello World! i work!")
    
    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print('Received command: ' + cmd)
            self.do_command(e, cmd)
        return


    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        if nick == "tremorbot":
            return
        
        if cmd == "github":
            c.privmsg(self.channel, "https://github.com/TremorAi/LearningPython")

        elif cmd == "setproject":
            self.project = e.arguments[0][11:]

        elif cmd == "project":
            c.privmsg(self.channel, f"{self.project}")

        elif cmd == "time":
            c.privmsg(self.channel, str(datetime.datetime.now()))

        
        
        # elif cmd == "poll":
        #     self.poll == e.arguments[0][5:]

        else:
            c.privmsg(self.channel, f"{e.arguments} not understood!")

def main():
    channel = config.channel
    username = config.username
    password = config.password

    bot = TwitchBot(username, password, channel)
    bot.start()       
        
if __name__ == "__main__":
    main()
