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
# Global constants for game balance
fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        # Basic character attributes
        self.name = name
        # Private attributes using double underscore for encapsulation
        self.__stamina = stamina
        self.__intelligence = intelligence
        
        # Derived attributes calculated from base stats
        # Intelligence determines mana pool (10 mana per intelligence point)
        self.mana = self.__intelligence * 10
        # Stamina determines health pool (100 health per stamina point)
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        # Check if wizard has enough mana to cast
        if self.mana < fireball_cost:
            # Raise exception if wizard doesn't have enough mana
            raise Exception(f"{self.name} cannot cast fireball")
        # Deduct mana cost from caster
        self.mana -= fireball_cost
        # Apply damage to target wizard
        target.get_fireballed()

    def is_alive(self):
        # Simple health check - wizard is alive if health is above 0
        return self.health > 0

    def get_fireballed(self):
        # Reduce health when hit by a fireball
        self.health -= fireball_damage

    def drink_mana_potion(self):
        # Restore mana when drinking a potion
        self.mana += potion_mana
