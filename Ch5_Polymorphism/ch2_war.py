"""
===
War
===

Let's extend our Card logic to a fully-fledged game of War.

----------
Assignment
----------

The "battle" logic has already been implemented for you in the War class. However,
for it to work we need to complete the CardGame, and War classes.

--------------------------
CardGame Class Constructor
--------------------------

The CardGame class is a base (parent) class that will be used to implement 
specific types of card games.

    * Initialize a deck instance variable to a DeckOfCards.
    * Shuffle the deck!

The .play() method just prints "Nothing to play..." because it's intended to be 
overridden by child classes.

---------------------
War Class Constructor
---------------------

War inherits from CardGame, after all, it's a specific type of card game. 
It should:

    * Call the CardGame constructor to initialize the deck.
    * Create a player1_hand instance variable and set it to an empty list.
    * Create a player2_hand instance variable and set it to an empty list.

---------------------
War Class play Method
---------------------

    * Use the __deal_hand helper method to deal 5 cards to player 1.
    * Do the same for player 2.
    * Once new hands have been dealt, call the __battle method.

-----------------------------------
War Class __deal_hand Helper Method
-----------------------------------

    * Use the deck's deal_card() method to deal 5 cards to the hand.
"""

import random


class CardGame:
    # Base class provides common card game infrastructure,
    # allowing for easy extension to other card games beyond War
    def __init__(self):
        self.deck = DeckOfCards()
        self.deck.shuffle_deck()

    def play(self):
        print("Nothing to play...")


class War(CardGame):
    def __init__(self):
        super().__init__()
        self.player1_hand = []
        self.player2_hand = []

    def play(self):
        # Game starts with 5 cards per player to create quick, engaging rounds
        # while leaving enough cards in deck for extended gameplay
        self.__deal_hand(self.player1_hand)
        self.__deal_hand(self.player2_hand)
        self.__battle()

    def __deal_hand(self, hand):
        # Private helper method ensures encapsulation of dealing logic
        # and maintains consistency across all dealing operations
        for i in range(5):
            hand.append(self.deck.deal_card())

    # don't touch below this line

    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0
        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            if len(self.player1_hand) == 0:
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()
            if len(self.player2_hand) == 0:
                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")
            if card1 > card2:
                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:
                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:
                ties += 1
                print("Tie! Both players draw a card and play again")
        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def index_of(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __cmp(self, other):
        self_suit_i = index_of(SUITS, self.suit)
        other_suit_i = index_of(SUITS, other.suit)
        self_rank_i = index_of(RANKS, self.rank)
        other_rank_i = index_of(RANKS, other.rank)
        if self_rank_i > other_rank_i:
            return "gt"
        if self_rank_i < other_rank_i:
            return "lt"
        if self_suit_i > other_suit_i:
            return "gt"
        if self_suit_i < other_suit_i:
            return "lt"
        return "eq"

    def __eq__(self, other):
        return self.__cmp(other) == "eq"

    def __gt__(self, other):
        return self.__cmp(other) == "gt"

    def __lt__(self, other):
        return self.__cmp(other) == "lt"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)


def test(seed):
    random.seed(seed)
    war = War()
    war.play()


def main():
    test(1)
    test(2)


main()