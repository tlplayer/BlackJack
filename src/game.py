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


#If the dealer busts give everyone who hasn't busted yet 5 dollars
	def dealer_bust(self):
		self.dealer.bust()
		for key in self.players:
			if self.players[key].state == True:
				self.dealer.money -= 5
				self.players[key].money += 5

	#What this does is check that all players are either staying or 
	#The dealer has busted  
	def check_round(self):
		if self.dealer.state == False:
			self.dealer_bust()
		else:
			for key in self.players:
				if self.players[key].stay == True:
    					if


#Prompts each player in the dictionary for their response	
	def play(self):
		for key in self.players:
			if self.players[key].stay == False:
				self.players[key].prompt()
		if self.dealer.stay == False:
			self.dealer.prompt()


###############################################################################
#GAME Utility FUNCTIONS:
###############################################################################

#This one clears all players.
	def new_game(self):
		for key in self.players:
			self.players[key].new_hand()
			self.players[key].deal()
			self.players[key].prompt()
		self.dealer.new_hand()
		self.dealer.deal()
		self.dealer.prompt()


#This one makes a new player could probably use the users username but whatevs
	def new_player(self):
		id = input("Enter your name: ")
		self.players.update({id:Player(self.money,id,self.deck)})



###############################################################################
#PRINTING FOR ALL PLAYERS:
###############################################################################

	def print_all(self):
		for key in self.players:
			self.players[key].print_cards()
		self.dealer.print_dealer()