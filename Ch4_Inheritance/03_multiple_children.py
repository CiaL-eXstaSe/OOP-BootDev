"""
===============================
Multiple Children
===============================

So far we've worked with linear class inheritance, but usually, inheritance 
hierarchies form trees, not lines. A parent class can have multiple children.

-----------------
Assignment
-----------------
The Archer class should inherit from Hero. Ensure the following requirements 
from the game designers are completed:

* Archer should inherit from Hero
* Archer should set up the hero's name and health
* Set a private "number of arrows" variable that can be passed in as a third 
  parameter to the constructor
* Create a shoot method that takes a target hero as input. If there are no 
  arrows left, raise a not enough arrows exception. Otherwise, remove an 
  arrow and deal 10 damage to the target hero
"""

# Base class for all hero types
# Uses private attributes for encapsulation
class Hero:
    def __init__(self, name, health):
        # Private attributes denoted by double underscore
        # Prevents direct access from outside the class
        self.__name = name
        self.__health = health

    # Getter method for the private name attribute
    # Provides controlled access to the name
    def get_name(self):
        return self.__name

    # Getter method for the private health attribute
    # Allows other classes to check but not directly modify health
    def get_health(self):
        return self.__health

    # Method to reduce hero's health when damaged
    # Allows controlled modification of the private health attribute
    def take_damage(self, damage):
        self.__health -= damage


# Archer class inherits from Hero (child class)
class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        # Call parent class constructor first using super()
        # This sets up the base hero attributes (name and health)
        super().__init__(name, health)
        # Add archer-specific private attribute for arrows
        self.__num_arrows = num_arrows

    def shoot(self, target):
        # Check if we have any arrows left (0 or negative)
        # Using <= 0 instead of < 1 because:
        # 1. It's more intuitive to read
        # 2. It defensively handles negative values
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        # Reduce arrow count and deal damage to target
        self.__num_arrows -= 1
        target.take_damage(10)
        # Return a message describing the action
        return f"{target.get_name()} was shot by 1 arrow"
