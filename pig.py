import random

class Die:
    """
    A Die has one method, roll(), that returns a random number between 1 and 6.
    """
    def __init__(self):
        pass
    
    def roll(self):
        return random.randint(1, 6)

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

class Player:
    """
    A Player has a score and plays the game until their score is 100 or above.
    """
    def __init__(self):
        """
        Parameters:
        - score -- the sum of the player's Turn scores, initialized to 0
        """
        self.score = 0

    def add_turn_score_to_score(self, turn_score):
        self.score += turn_score

    def is_winner(self):
        return self.score >= 100

    def wants_to_roll(self, turn):
        while True:
            roll_or_hold = input("Do you want to (r)oll or (h)old? ")
            if roll_or_hold:
                if roll_or_hold.lower()[0] in ['r', 'h']:
                    return roll_or_hold == 'r'
            else:
                print("I don't understand, please try again.")

class ComputerPlayer(Player):
    """
    A ComputerPlayer will always roll will if their turn score is less than 20.
    """
    def wants_to_roll(self, turn):
        return turn.score <= 20

def play_game():
    # set up game
    die = Die()
    game = Game(die)
    first_player, second_player = game.determine_order_of_players()
    
    # first player plays turn
    while not game.has_winner():
        game.play_turn(first_player)
        game.play_turn(second_player)
        game.display_scores()

    game.display_winner()

if __name__ == "__main__":
    play_game()
