__author__ = "tremor"
test = "meh"
import random as rand

class player:
	def __init__(self, name, hp, dmg, defense):
		self.hp = hp
		self.name = name
		self.dmg = dmg
		self.defense = defense


	def takedamage(self, dmg):
		defense = rand.randint(0, self.defense)
		self.hp = max(0, self.hp - (dmg-defense))

	def isalive(self):
		return self.hp > 0

	def printinfo(self):
		print(f"{self.name} {self.hp}")

	def miss(self):
		print(f"{self.name} missed..")


def main():
	player1 = player("tim", 150, 20, 10)
	player2 = player("jim", 150, 20, 10) # not op


	while player1.isalive() and player2.isalive():

		if rand.randint(0,10) % 2 == 0:
			player2.takedamage(player1.dmg)
			player2.printinfo()
		else:
			player2.miss()

		if rand.randint(0,10) % 2 == 0:
			player1.takedamage(player2.dmg)
			player1.printinfo()
		else:
			player1.miss()

	if player1.isalive():
		print(f"{player1.name} won!")
	elif player2.isalive():
		print(f"{player2.name} won!")	



if __name__ == '__main__':
			main()