Class-Responsibility-Collaborators

You are going to implement a version of the game of Pig in Python. Here's how the game works.

Two players are trying to reach 100 points first. On a player's turn, they roll a die over and over until they roll a 1 (a "pig") or they choose to hold. If they hold, they add the sum of their rolls to their score. If they roll a 1, they get no points. After a 1 is rolled or the player holds, the other player takes their turn.

The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)

In your implementation, there will be one human player and one computer player. The computer player will always hold until they roll a total of 20 points.

Classes:
Game
    Responsibilities:
        - create two opponents (Players)
        - randomly choose a Player to go first
        - keep track of Players' overall scores
        - determine winning Player

    Collaborators:
        - Player

Player
    Responsibilities:
        - roll Die
        - hold

    Collaborators:
        - Die

Turn
    Responsibilities:
        - track sum of of Players' Die rolls
    
    Collaborators:
        - Player
        - Die

Die
    Responsibilities:
        - return random number between 1 and 6


Nouns:
Game
Player
Points
Turn
Die

Verbs:
Players "reach" 100 points
Players "take" a turn
Players "hold"
Players "roll" Dice
Players "add" their Scores
Game randomly "chooses" a Player

1. Create two players
2. Decide which player goes first
    - player one rolls a die
    - player two rolls a die
    - if player one's roll > player two's roll, player one goes first. else, player two goes first
3. player with first turn goes first
4. player takes a turn:
    - rolls die
    - decides to hold or roll again (loop until hold or rolls 1)
    - if hold: turn ends and turn score is added to player overall score
    - if roll 1: turn ends
5. player with second turn goes second
6. player takes a turn:
    - rolls die
    - decides to hold or roll again (loop until hold)
    - if hold: turn ends and turn score is added to player overall score
    - if roll 1: turn ends
7. game ends when one player reaches 100
