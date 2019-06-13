Class-Responsibility-Collaborators:

Player, ComputerPlayer
    Responsibilities:
        - determine if roll or hold
        - keep track of overall score
        - determine if winner

    Collaborators:

Die
    Responsibilities:
        - return random number between 1 and 6

    Collaborators:

Game
    Responsibilities:
        - create two opponents (Players)
        - randomly choose a Player to go first
        - keep track of Players' overall scores
        - display Players' overall scores
        - play Turns until there is a winner
        - determine winning Player

    Collaborators:
        - Player, ComputerPlayer
        - Die
        - Turn

Turn
    Responsibilities:
        - track sum of Players' Die rolls
        - display sum of Players' Die rolls

    Collaborators:
        - Player