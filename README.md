# CardGame

Create a Card class containing:
- A color
- A number
- A symbol

Create a Board class containing:
- A list of Player nammed players
- a list of active Card (the 6 last played card are active) nammed active_cards
- a list of played Card (should not contain the 6 last cards, those should be in the active list) nammed played_cards

Create a class Player containing:
- A name nammed name
- A list of Card (each player start with 10 Card) nammed cards
- A play() method that throw a Card in the Board
- A suffle() method that shuffle all the Card of the plater

Create a loop so each player play() turn by turn until they don't have any Card left.
At the end of each turn, print the played card history and the active cards.

Add typing and docstrings.

You should use 2 files: 1 (utils.py) containing all your classes and 1 containing the loop (main.py). (import the classes in main.py)
