#Timothy Player 
#CS302 final project
#This module contains dealer functions such as hit, 
#deal initialize for the game class and dealer info.


import random

#Let's break down this class. Firstly the money 
#is a adjustable for convenience of the class master class
#The meat of it comes down to hit or stay, with utility 
#of betting and special cases of aces.
class Dealer:
	#intialize the dealer's money, name i.e. id.
	#They start with no cards until buy in

###############################################################################
#CONSTRUCTOR: Takes the dealers name and the deck of cards as is.
#			  Note the dealer's cash is 0 because we only care about what
#			  it makes vs what it loses.
###############################################################################


	def __init__( self, id, deck = []):
		self.money = 0
		self.id = id
		self.cards = []
		self.deck = deck
		self.standing = 0
		self.stay = False
		self.busted = False

###############################################################################
#I/O FUNCTIONS: This should be changed for the Flask hooking up.
###############################################################################

	#This is a dummy version until I figure out how the hell I get TF to work with
	#Flask
	def prompt(self):
		if self.standing >= 16:
			self.stay
			print("Dealer has stayed.")
		else:
			self.hit()
			print("Dealer has hit")
			self.print_cards()

###############################################################################
#BLACK JACK GAME FUNCTIONS: Draw, hit, deal, tally...
###############################################################################


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
			self.print_cards()
			self.bust()


	#Calls hit twice
	def deal(self):
		for i in range(2):
			self.hit()


	#Helper function to get total of dealer's cash
	def tally(self):
		self.standing = 0
		for i in range(len(self.cards)):
			value = self.cards[i]%13+1
			if value == 1: 
				self.standing += 11 if self.standing < 11 else 1
			else:
				self.standing += value if value < 10 else 10


	#If the dealer busts remove their bet from their
	#account. cards are not returned to deck.
	def bust(self):
		self.standing = 0
		self.busted = True
		self.stay = True
		self.cards.clear()
		self.print_bust()

	def new_hand(self):
		self.busted = False
		self.stay = False
		self.bet = 0
		self.standing = 0
		self.cards.clear()
		
		self.deal()

###############################################################################
#PRINT FUNCTIONS
###############################################################################


	#Prints the Player's cards and earnings and bet.
	def print_dealer(self):
		self.print_cards()
		
	#Print all the dealer's cards
	def print_cards(self):
		print("Player",self.id,"has cards:")
		for i in range(len(self.cards)):
			self.print_card(self.cards[i])
		self.print_score()

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
			value += 1
			print(value, " of ", suit_str)
		elif value == 10:
			print("Jack of ", suit_str)
		elif value == 11:
			print("Queen of ", suit_str)
		elif value == 12:
			print("King of ", suit_str)

	#Helper for most functions to declare when a dealer has bust.
	def print_bust(self):
		print("Dealer has busted.")

	#Print the user's score.
	def print_score(self):
		print("Dealer {}'s score: {}".format(self.id,self.standing))
