# import dedent function from textwrap module to fix indentation of multi-line strings
from textwrap import dedent

# import get_terminal_size function from os to center console output
from os import get_terminal_size

from player import Player, ComputerPlayer

class Game:
    """
    A Game is given a Die and controls the creation of players and their turns of the game 'Pig'
    """
    def __init__(self, die):        
        """
        Parameters:
        - die -- the die used in the game
        """
        self.die = die
        self.human_player = Player()
        self.computer_player = ComputerPlayer()
    
    def display_welcome(self):
        print(f"{'Welcome to Pig!':^{get_terminal_size().columns}}")

    def display_instructions(self):
        print(f"{'For each turn, you will choose to either roll a die or hold to end the turn.':^{get_terminal_size().columns}}")
        print(f"{'If you roll a 1, your turn will be ended and you will get no points for that turn.':^{get_terminal_size().columns}}")

    def determine_order_of_players(self):
        """
        Have each player roll a die; return the player with the highest roll.
        """
        if self.die.roll() > self.die.roll():
            print("You will go first.")
            return self.human_player, self.computer_player
        else:
            print("Computer player will go first.")
            return self.computer_player, self.human_player

    def play_turn(self, player):
        # instantiate new Turn with Player
        turn = Turn(player)

        # while Player wants to roll, roll die and add to turn score
        # if a 1 is rolled (a "Pig") then set turn score to 0 and end turn
        # add turn score to player score when done rolling
        while player.wants_to_roll(turn):
            roll_value = self.die.roll()
            print(f"Roll: {roll_value}")
            if roll_value == 1:
                print("You rolled a Pig!")
                turn.score = 0
                break
            turn.add_roll_to_score(roll_value)
            print(f"Turn total score: {turn.score}")
        player.add_turn_score_to_score(turn.score)
        print(f"New score: {player.score}")

    def display_scores(self):
        print("Scores:")
        print(f"Player one: {self.human_player.score}")
        print(f"Player two: {self.computer_player.score}")

    def has_winner(self):
        return self.human_player.is_winner() or self.computer_player.is_winner()

    def display_winner(self):
        if self.human_player.is_winner():
            print(f"Player One is the winner!")
        elif self.computer_player.is_winner():
            print(f"Player Two is the winner!")

class Turn:
    """
    A Turn represents a single round of the game 'Pig' and keeps score for the round
    Each turn, a Player rolls a Die and determines to 'Hold' (end the Turn) or roll again.
    """
    def __init__(self, player):
        self.player = player
        self.score = 0

    def display_turn_score(self):
        print(f"Turn score: {self.score}")

    def add_roll_to_score(self, roll_value):
        self.score += roll_value