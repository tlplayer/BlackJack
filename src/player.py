#Timothy Player 
#CS302 final project
#This module contains player functions such as hit, 
#deal initialize for the game class and player info.
#I'll see if I can add some analytics on hit stay ratio and or other stuff.

import random

#Let's break down this class. Firstly the money 
#is a adjustable for convenience of the class master class
#The meat of it comes down to hit or stay, with utility 
#of betting and special cases of aces.
class Player:
	#intialize the player's money, name i.e. id.
	#They start with no cards until buy in
	def __init__( self, money, id, deck = []):
		self.money = money
		self.id = id
		self.cards = []
		self.deck = deck
		self.standing = 0
		self.bet = 0
		self.bust = 0
	#Takes a card from the deck that is not a 1 and returns index.
	def draw(self):
		tmp = 0
		#Draw look randomly until there's something that no one else has. 
		while (tmp == 0):
			index = random.randrange(len(self.deck))
			tmp = self.deck[index]
		self.deck[index] = 1
		return index
	#Gives one card randomly from the deck without replacement.
	def hit(self):
		if self.standing <= 21:
			card = self.draw() 
			self.cards.append(card)
			self.sum()
		if standing > 21:
			self.bust()
	#Calls hit twice
	def deal(self):
		self.bust = 0
		for i in range(2):
			self.hit()
	#Prints the Player's cards and earnings and bet.
	def print(self):
		for i in range(cards):
			print()
	#Helper function to get total of player's cash
	def sum(self):
		self.standing = 0
		for i in range(len(self.cards)):
			value = self.cards[i]%13+1
			if value == 1: 
				self.standing += 11 if self.standing < 11 else 1
			else:
				self.standing += value if value < 10 else 10
	#If the player busts remove their bet from their
	#account. cards are not returned to deck.
	def bust(self):
		self.standing = 0
		self.cards.clear()
		self.money -= self.bet
"""
"""
#This is a little test code for the class to test that changing the deck changes
#the sub classes decks.
deck = [0]*52
x = Player(50,"Timothy", deck)
print(x.money)
print(x.id)
print(x.deck)
deck[0] = 1
print(x.deck)
x.deal()
print(x.cards)
print(x.standing)

