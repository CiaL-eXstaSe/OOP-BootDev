"""
=================
Constructors (or Initializers)
=================
It's rare in the real world to see a class that defines properties the way we've been doing it:
"""

class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2

"""
-----------
Constructors
-----------
It's more practical to use a constructor. In Python, if you name a method __init__, 
that's the constructor and it is called when a new object is created.

So, with a constructor, the code would look like this:
"""

class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2

"""
-----------------
Configurable Parameters
-----------------
Now we can make the starting armor and number of weapons configurable by passing parameters to the constructor!
This allows us to create different soldiers with different starting values.
"""

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"

"""
----------
Assignment
----------
Add a constructor to our Wall class. It should take depth, height and width as parameters, 
in that order, and set them as properties. It should also compute an additional property 
called volume. Volume is the depth times height times width.
"""

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

wall = Wall(10, 5, 2)
print(wall.volume)
# prints "100"