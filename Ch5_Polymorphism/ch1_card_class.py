"""
===============
Card Class
===============

We'll take a break from Age of Dragons to work on a simple deck of cards.

---------------
Assignment
---------------

Complete the Card class.

    Define a constructor that takes rank and suit as parameters 
    and sets rank, suit, rank_index, and suit_index instance variables.

You will need the indexes of the ranks, and suits to help you compare them 
against each other. Keep in mind that a rank and a suit are just strings 
within a list.

    Overload the following comparison operators:

    ==: eq
    >: gt
    <: lt

---------------
Ranking the Cards
---------------

A card is "greater than" another card if it has a higher rank. However, 
if the ranks are the same, the card with the higher suit is "greater than" 
the other card. This same logic applies to the "less than" operator. 
The "equal to" operator should check that the rank AND suit are equal.

The suits and ranks are defined as global variables. The lower the index, 
the lower the rank or suit.

---------------
Tips
---------------

The .index list method is very useful when trying to determine the index 
of an element in a list.
"""

Card Class

We'll take a break from Age of Dragons to work on a simple deck of cards.
Assignment

Complete the Card class.

    Define a constructor that takes rank and suit as parameters and sets rank, suit, rank_index, and suit_index instance variables.

You will need the indexes of the ranks, and suits to help you compare them against each other. Keep in mind that a rank and a suit are just strings within a list.

    Overload the following comparison operators:

    ==: eq
    >: gt
    <: lt

Ranking the Cards

A card is "greater than" another card if it has a higher rank. However, if the ranks are the same, the card with the higher suit is "greater than" the other card. This same logic applies to the "less than" operator. The "equal to" operator should check that the rank AND suit are equal.

The suits and ranks are defined as global variables. The lower the index, the lower the rank or suit.
Tips

The .index list method is very useful when trying to determine the index of an element in a list.