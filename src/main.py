#Timothy Player
#Main python script which calls the game and tests stuff. might link stuff
#through json with the server.

from game import Game


G = Game(50)

G.new_player()

play = input("Play a game? (Y/N)")

while play != "N":
    if play == "Y":
        G.new_game()

        while G.check_round() == True:
            G.print_all()
            G.play()
        G.round_over()
    play = input("Play another round? (Y/N)")
G.game_over()
