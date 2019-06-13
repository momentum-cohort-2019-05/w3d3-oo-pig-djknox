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
        self.player_one = Player()
        self.player_two = Player()

    def determine_order_of_players(self):
        """
        Have each player roll a die; return the player with the highest roll.
        """
        if self.die.roll() > self.die.roll():
            print("Player One will go first.")
            return self.player_one, self.player_two
        else:
            print("Player Two will go first.")
            return self.player_two, self.player_one

    def play_turn(self, player):
        # instantiate new Turn with Player
        turn = Turn(player)

        # while Player wants to roll, roll die and add to turn score
        # add turn score to player score when done rolling
        while player.wants_to_roll():
            roll_value = self.die.roll()
            if roll_value == 1:
                print("You rolled a Pig!")
                turn.score = 0
                break
            turn.add_roll_to_score(roll_value)
            print(f"Turn total score: {turn.score}")
        player.add_turn_score_to_score(turn.score)
        print(f"Player score: {player.score}")

    def has_winner(self):
        return self.player_one.is_winner() or self.player_two.is_winner()

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
        if roll_value == 1:
            self.score = 0


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

    def wants_to_roll(self):
        invalid_response = True
        while invalid_response:
            roll_or_hold = input("Do you want to (r)oll or (h)old? ").lower()[0]
            if roll_or_hold in ("r", "h"):
                return roll_or_hold == 'r'
            else:
                print("I don't understand, please try again.")
        

def play_game():
    # set up game
    die = Die()
    game = Game(die)
    first_player, second_player = game.determine_order_of_players()
    
    # first player plays turn
    while not game.has_winner():
        game.play_turn(first_player)
        game.play_turn(second_player)


if __name__ == "__main__":
    play_game()
