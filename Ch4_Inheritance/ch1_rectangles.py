'''
===================
Rectangles
===================

You discovered that to properly calculate army formations in the game, you needed to be able to get the area and perimeter
of squares and rectangles of various sizes.

-----------------
Challenge
-----------------
Finish implementing the empty methods of the Rectangle and Square classes. All squares are rectangles, but not all
rectangles are squares.

Note: Due to inheritance of methods, the Square class should only need to implement the __init__ method.
'''

class Rectangle:
    def __init__(self, length, width):
        # Using separate length and width parameters allows for flexible rectangle dimensions
        # while maintaining geometric accuracy
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        # Square inherits from Rectangle to follow the "is-a" relationship principle
        # and promote code reuse since a square is a special case of a rectangle
        # where length equals width
        super().__init__(length, length)
