"""
===============================
Wizard Duel
===============================

A magical combat system where wizards can cast fireballs at each other.

---------------------------------
Assignment Details
---------------------------------
Complete two core methods:
    1. cast_fireball
    2. is_alive

---------------------------------
Method Specifications
---------------------------------

cast_fireball:
    - Check if wizard has enough mana (fireball_cost)
    - If insufficient mana: raise Exception with message "{name} cannot cast fireball"
    - If sufficient mana:
        * Reduce mana by fireball_cost
        * Call get_fireballed on target wizard

is_alive:
    - Return True if health > 0
    - Return False otherwise
"""

Wizard Duel

Let's give our wizards the ability to launch fireballs at each other.
Assignment

Complete the cast_fireball and is_alive methods.
cast_fireball

If there isn't enough mana to cast a fireball (see fireball_cost at the top of the file), raise an Exception with the message ____ cannot cast fireball, where ____ is the wizard's name.

If the wizard has enough mana, reduce their mana by the fireball_cost and make sure to call get_fireballed on the target wizard or they'll be stuck in an endless battle.
is_alive

This method should return True if the wizard's health is greater than 0, and False otherwise.
