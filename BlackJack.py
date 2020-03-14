#Timothy Player
#Final Project sub project for 
#demo game for micro Bat game engine.

import random


#Take the number of players instantiate the array of cards 
#and supply 
def main():
	#Create a deck of 52 cards, the cards are one of the thirteen
	#types.
	cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	deck = [0]*52
	i = 0
	#Get user input of how many players. and give everyone $50
	num_players = int(input("Enter number of players:\n"))	
	money = [50]*num_players
	
	#Deal out random cards to all players. 
	for i in range(num_players):
		#Generate two random numbers
		first = random.randrange(0,52)
		second = random.randrange(0,52,1)

		#Ensure no duplicate numbers.
		while first == second:
			second = random(0,52,1)

		#Place the players number in deck to show that number is taken 
		if deck[first] != 0:
			deck[first] = i
		if deck[second] != 0:
			deck[second] = i

		#Calculate the score
		score = first%13 + second%13 + 2

		#Show the player what cards they have
		print("Player %d, your cards are: %c %c" % (i,cards[first%13],cards[second%13]))
		print("This totals to: %d" % (score))
"""
		#Hit until bust
		while score[i] < 21:
			response = input('"'Hit or stay?\n'"')
			if respone == 'H':
				first = random.randrange(0,52)
				if deck[first] != 0:
					deck[first] = i
			if response == 'S':
				break

"""		
#execute main()
main()	
