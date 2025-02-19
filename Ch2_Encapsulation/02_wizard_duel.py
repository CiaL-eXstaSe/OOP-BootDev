"""
WIZARD DUEL
===========

Description
-----------
Let's have ourselves a Wizard's duel.

Assignment
=========

Methods to Add
-------------
Add the following methods to the Wizard class:

get_fireballed()
---------------
* Operates on the instance of the class
* Takes no inputs 
* Returns no values explicitly
* Should remove 500 health from the wizard

drink_mana_potion() 
------------------
* Operates on the instance of the class
* Takes no inputs
* Returns no values explicitly
* Should add 100 mana to the wizard's reserves
"""

# Constants for game balance
fireball_damage = 500  # Amount of damage dealt by a fireball spell
potion_mana = 100     # Amount of mana restored by a mana potion


class Wizard:
    def __init__(self, name, stamina, intelligence):
        # Initialize a new Wizard with their base attributes
        # name: The wizard's name (public attribute)
        # stamina: Base stamina stat that determines health (private)
        # intelligence: Base intelligence stat that determines mana (private)
        self.name = name
        self.__stamina = stamina          # Private - implementation detail
        self.__intelligence = intelligence # Private - implementation detail
        
        # Derived public attributes calculated from base stats
        self.mana = self.__intelligence * 10  # Mana pool scales with intelligence
        self.health = self.__stamina * 100    # Health pool scales with stamina

    def get_fireballed(self):
        # Reduce the wizard's health when hit by a fireball spell
        # The damage amount is determined by the fireball_damage constant
        self.health -= fireball_damage

    def drink_mana_potion(self):
        # Restore mana to the wizard by drinking a mana potion
        # The amount restored is determined by the potion_mana constant
        self.mana += potion_mana