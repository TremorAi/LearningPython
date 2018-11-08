__author__ = "Tremor"

import asyncio
import config
from messages import Message
from fun_commands import *
from database import tbucks_update_loop


class AsyncTwitchBot:
    def __init__(self, reader, writer, channel):
        self.reader = reader
        self.writer = writer
        self.channel = channel

    def send_raw(self, message):
        self.writer.write(f"{message}\r\n".encode())
        
    def send_message(self, message):
        # self.writer.write(f"PRIVMSG {self.channel} {message}\r\n".encode())
        self.send_raw(f"PRIVMSG {self.channel} :{message}")

    def send_auth(self, username, password, channel):
        self.send_raw(f"PASS {password}")
        self.send_raw(f"NICK {username}")
        self.send_raw(f"JOIN {channel}")
        del globals()['config']

    async def run(self):
        self.send_auth(config.username, config.password, config.channel)
        # self.send_message(f"I have joined muahahahaa")
        while True:
            # if Message == True:
            #     pass
            line = (await self.reader.readline()).decode().strip()
            msg = Message(line)
            if msg.iscommand and msg.command in commands:
                asyncio.ensure_future(commands[msg.command].func(self, msg))
            elif db.command_exists(msg.command):
                self.send_message(db.get_command(msg.command))
            elif msg.iscommand:
                self.send_message(f"{msg.command} is not a valid command.")
                

            if 'PING' in line:
                self.send_raw('PONG :tmi.twitch.tv')
        
async def main():
    host = "irc.chat.twitch.tv"
    port = 6667
    reader, writer = await asyncio.open_connection(host, port)
    channel = "#tremorai"
    bot = AsyncTwitchBot(reader, writer, channel)
    asyncio.ensure_future(tbucks_update_loop())
    await bot.run()
    
    
if __name__ == "__main__":
    asyncio.run(main())