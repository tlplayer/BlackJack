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
		standing = 0
	def deal():
		bust = 0
		cards.append(deck.pop())
		cards.append(deck.pop())
	def hit():
		if standing <= 21 and deck.size() != 0:
			cards.append(deck.pop())
			standing = self.sum()
	def print():
		for i in range(cards):
			print()
	def sum():
		for i in range(cards):
			sum = 
