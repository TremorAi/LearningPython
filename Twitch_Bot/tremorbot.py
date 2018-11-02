__author__ = "Tremor"

import socket

class TwitchBot:
    def __init__(self, username, password, channel):
        self.username = username
        self.password = password
        self.channel = channel
        
        host = "irc.chat.twitch.tv"
        port = 6667

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
    
    def sendauth(self):
        return
    
    def start(self):
        self.sendauth()
        data = self.socket.recv(1024)
    
    def joinchannel(self):
        
        return
