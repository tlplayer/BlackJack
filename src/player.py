#Timothy Player 
#CS302 final project
#This module contains player functions such as hit, 
#deal initialize for the game class.

#Let's break down this class. Firstly the money 
#is a adjustable  for the dealer.
class Player:
	def __init__( self, money, id, deck = []):
		self.money = money
		self.id = id
		cards = []
		self.deck = deck
		standing = 0
		bet = 0
	def deal():
		bust = 0
		cards.append(deck.pop())
		cards.append(deck.pop())
	#
	def hit():
		if standing <= 21 and deck.size() != 0:
			cards.append(deck.pop())
			standing = self.sum()
	#Prints the Player's cards and earnings and bet.
	def print():
		for i in range(cards):
			print()
	#Helper function to get total of player's
	#cash
	def sum():
		for i in range(cards):
			sum += cards[i] 
	#If the player busts remove their bet from their
	#account.
	def bust(bet):
		standing = 0
		money -= bet
