"""
ENCAPSULATION
============

Basic Concept
------------
Encapsulation is the practice of hiding complexity inside a "black box" so that it's 
easier to focus on the problem at hand.

Function Example
---------------
The most basic example of encapsulation is a function. The caller of a function 
doesn't need to worry too much about what happens inside, they just need to 
understand the inputs and outputs.

Example:
    acceleration = calc_acceleration(initial_speed, final_speed, time)

To use the calc_acceleration function, we don't need to think about every individual 
line of code inside the function. We just need to know that if we give it the inputs:
    * initial_speed
    * final_speed
    * time
Then it will give us the correct acceleration as an output.

PUBLIC AND PRIVATE
================

Access Modifiers
---------------
By default, all properties and methods in a class are public. That means that you 
can access them with the . operator:

Example:
    wall.height = 10
    print(wall.height)  # 10

Private Members
--------------
Private data members are how we encapsulate logic and data within a class. To make 
a property or method private, you just need to prefix it with two underscores.
"""

# Example of private members - This is actual runnable code
class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

# Usage example
front_wall = Wall(10, 20)

# This results in an error
# print(front_wall.__armor)

# This works
print(front_wall.get_defense())  # 30

"""
We do this because, in this example, armor and magic_resistance are implementation 
details. After creating a Wall, they don't matter anymore. Now the game developers 
can just call get_defense and not worry about how it's calculated under the hood.

ASSIGNMENT
=========
Complete the Wizard class's constructor. It should set 2 private properties:
    * "stamina"
    * "intelligence"

Don't forget to make them private! Use the values passed into the constructor to 
set the properties.

It should also set 3 public properties:
    * name: Use the value passed into the constructor.
    * health: 100x the value of "stamina".
    * mana: 10x the value of "intelligence".
"""

# Your Wizard class implementation goes here
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * self.__stamina
        self.mana = 10 * self.__intelligence

    