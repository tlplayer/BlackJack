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

	#Takes a card from the deck that is not a 1 and returns index.
	def draw(self):
		tmp = 1
		#Draw look randomly until there's something that no one else has. 
		while (tmp == 1):
			index = random.randrange(len(self.deck))
			tmp = self.deck[index]
		self.deck[index] = 1
		return index

	#Gives one card randomly from the deck without replacement.
	def hit(self):
		if self.standing <= 21:
			card = self.draw() 
			self.cards.append(card)
			self.tally()
		if self.standing > 21:
			self.bust()

	#Calls hit twice
	def deal(self):
		for i in range(2):
			self.hit()

		#Helper function to get total of player's cash
	def tally(self):
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
		self.print_bust()

	#Prints the Player's cards and earnings and bet.
	def print(self):
		for i in range(cards):
			print()


	#Print all the player's cards
	def print_cards(self):
		print("Player",self.id,"has cards:")
		for i in range(len(self.cards)):
			self.print_card(self.cards[i])

	#Python apparently does not have a switch statement yikes.
	def print_card(self, index):
		value = index%13
		suit = index//13
		suit_str = ""
		if suit == 0:
			suit_str = "Hearts"
		if suit == 1:
			suit_str = "Spades"
		if suit == 2:
			suit_str = "Clubs"
		if suit == 3:
			suit_str = "Diamonds"
		if value == 0:
			print("Ace of ", suit_str)
		elif value < 10:
			++value
			print(++value, " of ", suit_str)
		elif value == 10:
			print("Jack of ", suit_str)
		elif value == 11:
			print("Queen of ", suit_str)
		elif vaalue == 12:
			print("King of ", suit_str)
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
x.hit()
print(x.cards)
print(x.standing)
x.print_cards()
