#This file hosts the game class with sub
#player class and the dealer class

from player import Player
from dealer import Dealer
import sys
import json


#This handles bets, ani-ups, and the pot.
class Game:
###############################################################################
#CONSTRUCTOR: Supplies players with cash, the deck, initializes an empty dictionary
#			  and creates the dealer Jeeves.
###############################################################################
	def __init__(self,money):
		self.deck = [0]*52
		self.money = money
		self.players = {}
		self.dealer = Dealer("Jeeves",self.deck)


###############################################################################
#GAME PRECEDURES:
###############################################################################

#Prompts each player in the dictionary for their response	
	def play(self):
		for key in self.players:
			key.prompt()
		self.dealer.prompt()

#This one clears all players.
	def new_game(self):
		for key in self.players:
			key.new_hand()
			key.prompt()

#This one makes a new player could probably use the users username but whatevs
	def new_player(self,id):
		id = scan("Enter your name: ")
		self.players.update({id:Player(self.money,id,self.deck)})

x = Game(50)

