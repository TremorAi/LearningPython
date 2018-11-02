__author__ = "tremor"

import requests
import sys
import irc.bot

class Twitchbot(irc.bot.SingleServerIRCBot):
	def __init__(self, username, client_id, token, channel):
		self.client_id = client_id
		self.token = token
		self.channel = '#' + channel

		url = 'https://api.twitch.tv/kraken/users?login=' + channel
		headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
		r = requests.get(url, headers=headers).json()
		self.channel_id = r['users'][0]['_id']

		server = 'irc.chat.twitch.tv'
		port = 6667
		print(f"Connecting to {server} on port {str(port)} ...")
		super().__init__(self, [{server, port, 'oauth:'+token}], username, username)

	def on_pubmsg(self, c, e):

		if e.arguments[0][:1] == "!":
			cmd = e.arguments[0].split(' ')[0][1:]
			print(f"Received command: {cmd}")
			self.do_command(e, cmd)

	def do_command(self, e, cmd):
		c  = self.connection

		if cmd == "title":
			url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
			headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
			r = requests.get(url, headers=headers).json()
			c.privmsg(self.channel, r['display_name'] + ' channel title is currently ' + r['status'])


def main():
	return


if __name__ == '__main__':
	main()