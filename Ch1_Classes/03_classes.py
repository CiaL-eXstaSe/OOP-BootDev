"""
========
Classes
========
A class is a special type of value in an object-oriented programming language like Python. 
It's similar to a dictionary in that it usually stores other types inside itself.

# Defines a new class called "Soldier"
class Soldier:
    health = 5
    armor = 3
    damage = 2

Just like a string, integer or float, a class is a type, 
but instead of being a built-in type, your classes are custom types that you define.

An object is just an instance of a class type. For example:

health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier type (class)

"Classes" are custom new types that we define as the programmer. 
Each new instance of a class is an "object".

--------
Example
--------
class Archer:
    health = 40
    arrows = 10

# Create several instances of the Archer class
legolas = Archer()
bard = Archer()

# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10

-----------
Assignment
-----------
Create a class called Wall on line 1. It should have a property called armor that is initialized to 10 and a height that starts at 5.
"""

# Define a Wall class with initial armor and height properties
class Wall:
    # Class properties with default values
    armor = 10    # Initial armor value
    height = 5    # Initial height value

# Create an instance of the Wall class
wall = Wall()
# Print the wall's properties to verify initialization
print(wall.armor)
print(wall.height)