"""
===============================
Bringing It Together in the Dragon Class
===============================

Let's bring all we've done together in the Dragon class. The Dragon class should 
override the Unit class's in_area method. Instead of checking if the center 
position of the Dragon is in the given area, we'll check if its big dragon body 
overlaps with the given area.

    Methods in parent classes often use pass to signal they should be overridden 
    in child classes. To override, create a method with the same name in the 
    child class.

-----------------
Assignment
-----------------

First, complete the Dragon's constructor. The dragon needs one more private data 
member: __hit_box. The hitbox is a Rectangle object. You've been provided with 
the height, width, and center position (pos_x, pos_y) of the dragon.

-----------------
in_area() method()
-----------------

Next, you'll need to override the in_area method that the Dragon class inherited 
from the Unit class. In the Dragon class' in_area method, create a new rectangle 
object with the given corner positions, and use the rectangle's overlaps method 
to check if the Dragon's self.__hit_box is inside it. This method should return 
a boolean value.

-----------------
Tips
-----------------

    Add half of the width to pos_x to find the right side.
    Subtract half of the width from pos_x to find the left side.
    Add half of the height to pos_y to find the top side.
    Subtract half of the height from pos_y to find the bottom side.
"""

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        # Using a Rectangle for hitbox enables efficient collision detection
        # and centralizes complex overlap calculations
        self.__hit_box = Rectangle(pos_x - width / 2, pos_y - height / 2, pos_x + width / 2, pos_y + height / 2)

    def in_area(self, x1, y1, x2, y2):
        # Override parent's point-based check with hitbox overlap
        # to account for dragon's physical size in the game world
        return self.__hit_box.overlaps(Rectangle(x1, y1, x2, y2))


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2