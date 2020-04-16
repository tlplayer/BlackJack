#Timothy Player
#Main python script which calls the game and tests stuff. might link stuff
#through json with the server.

from game import Game


G = Game(50)

G.new_player()

G.new_game()

G.print_all()
while G.check_round() == True:
    G.play()
G.round_over()

G.print_all()
