#Timothy Player 
#CS302 final project
#This module contains player functions such as hit, 
#deal initialize for the game class.

#Numpy Arrays
import numpy as np

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
		bust = 0
	#Takes a card from the deck that is not a 1 and returns index.
	def draw():
		while (card == 0):
			card = randrange(len(deck))
		deck[choice]
		return card
	#Calls hit twice
	def deal():
		bust = 0
		hit()
		hit()
		print()
	#Gives one card randomly from the deck without replacement.
	def hit():
		if standing <= 21 and deck.size() != 0:
			
			cards.append()
			standing += card%13 if card%13 < 10 else 10  
	#Prints the Player's cards and earnings and bet.
	def print():
		for i in range(cards):
			print()
	#Helper function to get total of player's cash
	def sum():
		for i in range(cards):
			standing += cards[i] 
	#If the player busts remove their bet from their
	#account.
	def bust(bet):
		standing = 0
		money -= bet
"""
This is a little test code for the class to test that changing the deck changes
the sub classes decks.
deck = [0]*52
x = Player(50,"Timothy", deck)
print(x.money)
print(x.id)
print(x.deck)
deck[0] = 1
print(x.deck)
"""
