#Timothy Player
#Final Project sub project for 
#demo game.

#Take the number of players instantiate the array of cards 
#and supply 
def main():
	#Create a deck of 52 cards, the cards are one of the thirteen
	#types.
	cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
	deck = [0]*52

	#Get user input of how many players. and give everyone $50
	num_players = int(input("Enter number of players:\n"))	
	score = [50]*num_players

#execute main()
main()	
