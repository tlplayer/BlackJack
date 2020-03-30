#This file hosts the game class with sub
#player class and the dealer class

import player
import dealer
import sys


#This handles bets, ani-ups, and the pot.
class Game:
	#Constructor for the game class supplies players with cash
	#and 
	def __init__(self,money):
		deck = [0]*52
		self.money = money
		self.players = {}
		self.dealer = dealer("Jeeves",self.deck)
	def play(self):
    	for key in players
			key.prompt()
		dealer.prompt()
	def new_game(self):
		for key in players:
			key.new_hand()
			key.prompt()
	def new_player(self,id):
		id = scan("Enter your name: ")
		self.players.update({id:player(self.money,id,self.deck)})
x = Game(1)
