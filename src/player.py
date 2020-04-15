#Timothy Player 
#CS302 final project
#This module contains player functions such as hit, 
#deal initialize for the game class and player info.
#I'll see if I can add some analytics on hit stay ratio and or other stuff.

import random

#Let's break down this class. Firstly the money 
#is adjustable for convenience of the class' master class
#The meat of it comes down to hit or stay, with utility 
#of betting and special cases of aces.
class Player:
	#intialize the player's money, name i.e. id.
	#They start with no cards until buy in The state
	#of the player determines if they are playing in the hand
	#or if they have 
	def __init__( self, money, id, deck = []):
		self.money = money
		self.id = id
		self.cards = []
		self.deck = deck
		self.standing = 0
		self.bet = 0
		self.state = True

###############################################################################
#GAME STATE FUNCTIONS
###############################################################################

	#If the player busts remove their bet from their
	#account. cards are not returned to deck.
	def bust(self):
		self.standing = 0
		self.cards.clear()
		self.money -= self.bet
		self.print_bust()
		return self.bet

	#They no longer can hit so there's that.
	def fold(self):
		self.state = False

	#Create a new hand and set the bet to 0.
	def new_hand(self):
		self.state = True
		self.bet = 0

	#If the player wins give them their money.
	def win(self):
		self.money += self.bet*3/2
		return 1

###############################################################################
#I/O FUNCTIONS
###############################################################################

#NOTE: need to change this for the flask part.

	#Prompt the player to anni up or hit or stay.
	#also handles Anniing
	def prompt(self):
		if self.bet == 0:
			response = input("Buyin? (Yes/No)")
			if response == "No":
				self.fold()
			else:
				self.anni(5)
		else:
			response = input("Hit or Stay?")
			if response == "Hit":
				self.hit()


###############################################################################
#Black Jack Parts.
###############################################################################

	def anni(self,wager):
		if wager <= self.money:
			self.bet = wager
			return 1
		else:
			print("Bet greater than {}".format(self.money))
			self.fold()
			return 0

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

	#Calls hit twice if the player hasn't folded.
	def deal(self):
		if state == True:
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
###############################################################################
#PRINTING FUNCTIONS
###############################################################################
	#Prints the Player's cards and earnings and bet.
	def print_player(self):
		self.print_cards()
		self.print_score()
		
	#Print all the player's cards
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

	#Helper for most functions to declare when a player has bust.
	def print_bust(self):
		print("Player", self.id,"has busted.")
		print("They lost:$", self.bet)

	#Print the user's score.
	def print_score(self):
		print("Player {}'s score: {}".format(self.id,self.standing))
