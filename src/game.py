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
			if self.players[key].busted == False:
				self.dealer.money -= 5*3/2
				self.players[key].win()

	#What this does is check that all players are either staying or 
	#The dealer has busted  If everyone has stayed the game isn't still going.
	# or if the dealer busts the game is also over.
	def check_round(self):
		if self.dealer.busted == True:
			self.dealer_bust()
		else:
			for key in self.players:
				if self.players[key].stay == False:
    					return True
		return False
			

	def round_over(self):
		for key in self.players:
			if (self.players[key].stay == True) and (self.players[key].standing > self.dealer.standing):
				self.players[key].win()


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
		self.deck = 52*[0]
		for key in self.players:
			self.dealer.money += self.players[key].new_hand()
		self.dealer.new_hand()



#This one makes a new player could probably use the users username but whatevs
	def new_player(self):
		id = input("Enter your name: ")
		self.players.update({id:Player(self.money,id,self.deck)})

	def game_over(self):
		for key in self.players:
			print("{} has ${}".format(self.players[key].id, self.players[key].money))
		print("The Dealer has a delta of ${}".format(self.dealer.money))

###############################################################################
#PRINTING FOR ALL PLAYERS:
###############################################################################

	def print_all(self):
		for key in self.players:
			self.players[key].print_cards()
		self.dealer.print_dealer()
