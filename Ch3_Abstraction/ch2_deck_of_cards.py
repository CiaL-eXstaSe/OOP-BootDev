"""
==================
Deck of Cards
==================

Assignment
----------
Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided 
for you as class variables. You won't need to modify them, but you will need to 
use them.

Constructor
----------
* Initialize a private empty list called cards
* Fill that empty list by calling the create_deck method within the constructor

create_deck(self)
----------------
This method should create a (Rank, Suit) tuple for all 52 cards in the deck and 
append them to the cards list.

Order matters! The cards should be appended to the list in the following order:
all ranks of hearts, then diamonds, then clubs, and finally spades. Within each 
suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

shuffle_deck(self)
-----------------
This method should use the random.shuffle() method (available from the random 
package) to shuffle the cards in the deck.

deal_card(self)
--------------
This method should .pop() the first card off the top of the deck (top of the deck 
is the end of the list) and return it. If there are no cards left in the deck the 
method should instead return None.
"""

import random


class DeckOfCards:
    # Class variables shared by all instances
    # Standard 52-card deck suits
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    # Card ranks from Ace (lowest) to King (highest)
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        # Initialize private cards list using double underscore for name mangling
        # This prevents direct access from outside the class
        self.__cards = []
        # Populate the deck with all 52 cards upon creation
        self.create_deck()

    def create_deck(self):
        # Create a full deck by combining each suit with each rank
        # Nested loops ensure we get all 52 combinations
        # Cards are stored as tuples of (rank, suit)
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        # Use Python's built-in random.shuffle to randomly reorder the cards
        # This modifies the list in-place
        random.shuffle(self.__cards)

    def deal_card(self):
        # Remove and return the last card from the deck (top of the deck)
        # If deck is empty (no cards left), return None
        # Using pop() without an index removes the last element
        return self.__cards.pop() if self.__cards else None

    # don't touch below this line

    def __str__(self):
        # String representation of the deck showing number of remaining cards
        return f"The deck has {len(self.__cards)} cards"