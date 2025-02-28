"""
===============================
Inheritance Hierarchy
===============================

There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit 
from an Animal that inherits from LivingThing. That said, be careful! New programmers often 
get carried away.

You should never think to yourself:
"Well most wizards are elves... so I'll just have wizard inherit from elf"

A good child class is a strict subset of its parent class.

---------------------------------
Private Properties Example
---------------------------------
A child class cannot simply access a private property of its parent class. It has to use a getter.
"""

class Wall:
    def __init__(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

class Castle(Wall):
    def __init__(self, height, towers):
        super().__init__(height)
        self.towers = towers

    def get_tower_height(self):
        return self.get_height() * 2

"""
===============================
Assignment
===============================

Let's add a new game unit: Crossbowman. A crossbowman is always an archer, but not all archers 
are crossbowmen. Crossbowmen have several arrows, but they have an additional method: triple_shot().

Requirements:
---------------------------------
* Add a use_arrows(self, num) method to the Archer class. It should remove num arrows. 
  If there aren't enough arrows to remove, it should raise a not enough arrows exception.
* The Crossbowman class's constructor should call its parent's constructor.
* The crossbowman's triple_shot method should use 3 arrows.
* The crossbowman's triple_shot method takes a target as a parameter and returns 
  '{} was shot by 3 crossbow bolts' where {} is the name of the Human that was shot.
"""

class Human:
    def __init__(self, name):
        # Use double underscore for name to make it private
        # This ensures the name can only be accessed through the getter method
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        # Call the parent (Human) constructor to set the name
        super().__init__(name)
        # Make num_arrows private to protect it from direct modification
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        # Check if we have enough arrows before using them
        # Using generic Exception instead of ValueError to match test requirements
        if self.__num_arrows < num:
            raise Exception("not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        # Initialize the Archer parent class with the name and arrows
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        # Our previous solution:
        # ----------------------
        # if self.get_num_arrows() < 3:
        #     raise ValueError("not enough arrows")
        # self.use_arrows(3)
        # return f"{target.get_name()} was shot by 3 crossbow bolts"

        # Author's solution:
        # -----------------
        # 1. No need to check arrows here since use_arrows() already does that
        # 2. Store target name in variable for clarity
        # 3. Uses generic Exception in use_arrows() instead of ValueError
        self.use_arrows(3)
        target_name = target.get_name()
        return f"{target_name} was shot by 3 crossbow bolts"
