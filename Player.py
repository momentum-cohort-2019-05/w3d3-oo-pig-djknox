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
    A ComputerPlayer inherits from Player and will always roll will if their turn score is less than 20.
    """
    def wants_to_roll(self, turn):
        return turn.score <= 20