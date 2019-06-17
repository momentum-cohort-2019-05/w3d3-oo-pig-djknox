# import randint from random for random number generation
from random import randint

class Die:
    """
    A Die has one method, roll(), that returns a random number between 1 and 6.
    """
    def __init__(self):
        pass
    
    def roll(self):
        return randint(1, 6)
