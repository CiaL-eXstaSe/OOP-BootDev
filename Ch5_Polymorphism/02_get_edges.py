"""
===============
Get Edges
===============

Remember that with normal "units" we were checking if their (x/y) point was within a 
rectangle (the Dragon's breath) to see if they were hit by the fire. With a dragon, 
because they're so big, we're going to check if the dragon's body (a rectangle) is 
within the fire (also a rectangle). The image below contains an example of fire 
breath hitting a dragon.

---------------
Assignment
---------------

In the next assignment, we'll be writing the overlap method itself, but first you're 
going to write a method to find the edges of a rectangle.

    The coordinates have now been made private members — we added two underscores to 
    them — so we need to write getter methods to access them.

First, let's set up some helper methods to find these edges.

    Write the following methods. What they do should be self-explanatory given their 
    names.
        get_left_x()
        get_right_x()
        get_top_y()
        get_bottom_y()

Remember that x1 OR x2 could be the "left x" based on its value on the Cartesian 
plane. The same goes for the y values. You may find Python's built-in min and max 
functions useful if you'd rather not use the comparison operators.

Note: The __repr__ method will be explained later in this chapter.
"""

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        # Using private members to enforce encapsulation for edge calculations
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # min/max functions allow rectangle points to be specified in any order
    # while still correctly identifying boundaries
    def get_left_x(self):
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
