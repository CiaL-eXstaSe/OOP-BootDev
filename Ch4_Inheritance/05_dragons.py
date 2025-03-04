"""
===============
Dragons
===============

In "Age of Dragons", there are Orcs, Humans, Goblins, Dragons, etc. All of those 
different creatures are called "units". At the moment, the only thing specific to 
a unit is that it has a position on the game map and a name.

Dragons, a specific type of unit, can breathe fire in a large area dealing damage 
to any units that are touched by its fiery blaze.

---------------
The Game Grid
---------------
Our game map is just a Cartesian plane.

===============
Assignment
===============

Complete the unit's in_area method and the dragon's breathe_fire method.

---------------
in_area
---------------
This method has four parameters, x_1, y_1, x_2, and y_2. The coordinates x_1 and 
y_1 represent the bottom-left corner of the rectangle, while x_2 and y_2 represent 
the top-right corner.

To determine if a unit is within or on the boundary of this rectangle, use the 
unit's position coordinates pos_x and pos_y. If the unit's position falls inside 
or on the edge of the rectangle, the method returns True. Otherwise, it returns 
False.

---------------
breathe_fire
---------------
This method causes the dragon to breathe a swath of fire in the target area. The 
target area is centered at (x,y). The area stretches for __fire_range in both 
directions inclusively.

For each unit in the units list, append that unit to a list if the unit is within 
the blast. Return the list of units hit by the blast.

---------------
Example of Fire Breath Hitting a Unit
---------------
The example above uses a __fire_range of 1 centered at (1, 1).

"""

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        # Position coordinates are public to allow for direct position checks
        # by other game systems (rendering, collision, etc.)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        # Using inclusive bounds (<=) to handle edge cases where units
        # are exactly on the boundary of an area
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        # Double underscore used for fire_range to prevent accidental modification
        # of this critical combat stat by derived classes
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        # Using a square area of effect for performance and simplicity
        # instead of a more realistic but computationally expensive circular area
        hit_units = []
        for unit in units:
            if unit.in_area(x - self.__fire_range, y - self.__fire_range, x + self.__fire_range, y + self.__fire_range):
                hit_units.append(unit)
        return hit_units
    
    
"""
Alternative Solution:

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_by_blast = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
        return hit_by_blast

Key Differences and Benefits:

1. in_area method formatting:
   - Breaks down logical conditions into separate lines for better readability
   - Uses explicit 'and' operators instead of Python's chained comparisons
   - Makes each condition more explicit and easier to understand
   - More maintainable if additional conditions need to be added

2. breathe_fire method differences:
   - Uses more descriptive variable names (hit_by_blast vs hit_units)
   - Stores the result of in_area check in a separate variable
   - Splits logic into smaller, more digestible steps
   - Easier to debug by inspecting the in_area variable

While both solutions are functionally identical, the alternative solution follows 
better software engineering practices with improved:
- Readability through proper line breaks and explicit conditions
- Maintainability
- Descriptive variable naming
- Debugging capabilities

In professional settings, this more verbose but clearer style would typically be 
preferred, as code is read much more often than it is written.
"""
    
    