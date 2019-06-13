#import classes for setting up a new game
from Die import Die
from Game import Game

def play_game():
    # set up game
    die = Die()
    game = Game(die)
    game.display_welcome()
    game.display_instructions()
    first_player, second_player = game.determine_order_of_players()
    
    # first player plays turn
    while not game.has_winner():
        game.play_turn(first_player)
        game.play_turn(second_player)
        game.display_scores()

    game.display_winner()

if __name__ == "__main__":
    play_game()
