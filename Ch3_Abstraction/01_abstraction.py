"""
===================
Abstraction
===================

Abstraction helps us handle complexity by hiding unnecessary details. Sounds like 
encapsulation, right? They're so similar that it's almost not worth worrying about 
the difference...almost.

-----------------------
Abstraction vs. Encapsulation
-----------------------

    Abstraction is about creating a simple interface for complex behavior. It focuses 
    on what's exposed.
    Encapsulation is about hiding internal state. It focuses on tucking implementation 
    details away so no one depends on them.

Abstraction is more about reducing complexity, encapsulation is more about maintaining 
the integrity of system internals.

-----------------------
Are We Encapsulating or Abstracting?
-----------------------

Both. Almost always we are doing both. Here's an example of using the random library 
to generate a random number:
"""

import random

attack_damage = random.randrange(5)

"""
Generating random numbers is a really hard problem. The operating system uses the 
physical hardware of the computer to create a seed for the randomness. However, the 
developers of the random library have abstracted that complexity away and encapsulated 
it within the simple randrange function. We just say "I want a random number from 0 to 4" 
and the library does it.

When writing libraries for use by other developers, getting the abstractions right is 
crucial because changing them later can be disastrous. Imagine if the maintainers of 
the random module changed the input parameters to the randrange function! It would break 
code all over the world.

-----------------------
Assignment
-----------------------

A Human class and its constructor have already been created for you. We don't want the 
other game developers using our Human class to have to worry about how humans move. 
We'll abstract that away from them by encapsulating the private __pos_x, __pos_y, 
and __speed variables.

Complete these methods:

    move_right(): Adds the human's speed to its x position
    move_left(): Subtracts the human's speed from its x position
    move_up(): Adds the human's speed to its y position
    move_down(): Subtracts the human's speed from its y position
    get_position(): Returns the x position and y position as a tuple
"""

class Human:
    # Constructor initializes a human with position and movement speed
    # Using double underscore for true private variables to prevent direct access
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x      # Private x-coordinate
        self.__pos_y = pos_y      # Private y-coordinate
        self.__speed = speed      # Private movement speed

    # Movement methods abstract away the complexity of position management
    # Each method updates the position by the speed value in the appropriate direction
    def move_right(self):
        self.__pos_x += self.__speed  # Increase x-coordinate to move right

    def move_left(self):
        self.__pos_x -= self.__speed  # Decrease x-coordinate to move left

    def move_up(self):
        self.__pos_y += self.__speed  # Increase y-coordinate to move up

    def move_down(self):
        self.__pos_y -= self.__speed  # Decrease y-coordinate to move down

    # Getter method provides a clean interface to access position
    # Returns a tuple to prevent direct modification of position values
    def get_position(self):
        return (self.__pos_x, self.__pos_y)