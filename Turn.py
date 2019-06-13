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