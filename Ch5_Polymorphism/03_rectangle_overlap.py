"""
===============================
Check If Rectangles Overlap
===============================

-----------------
Assignment
-----------------

Let's write the overlaps() method. It should check if this rectangle overlaps a given rectangle, rect. Return True if this rectangle overlaps any part of rect, including just touching sides, or False otherwise.

Here are four conditions that must all be True if this rectangle (A) overlaps or touches rect (B):

    A's left side is on or to the left of B's right side
    A's right side is on or to the right of B's left side
    A's top side is on or above B's bottom side
    A's bottom side is on or below B's top side
"""

class Rectangle:
    def overlaps(self, rect):
        # Using <= and >= instead of < and > to handle edge cases
        # where rectangles share edges or corners, which are considered overlapping
        return (
            self.get_left_x() <= rect.get_right_x() and
            self.get_right_x() >= rect.get_left_x() and
            self.get_top_y() >= rect.get_bottom_y() and
            self.get_bottom_y() <= rect.get_top_y()
        )

    # don't touch below this line

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

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"