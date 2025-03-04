"""
===================
What Is Polymorphism?
===================

While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful. Polymorphism is the ability of a variable, function or object to take on multiple forms.

    "poly"="many"
    "morph"="form".

For example, classes in the same hierarchical tree may have methods with the same name but different behaviors.

------------------
Different Forms
------------------

Let's look at a simple example.
"""

class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims

"""
The Dragon and Kraken child classes are overriding the behavior of their parent class's move() method.

------------------
Assignment
------------------

We're going to build hit-box logic for our game step by step, starting with a simple Rectangle.

Complete the __init__() method. Configure the class to have properties matching the variables passed into the constructor in this order:

    x1
    y1
    x2
    y2
"""

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
