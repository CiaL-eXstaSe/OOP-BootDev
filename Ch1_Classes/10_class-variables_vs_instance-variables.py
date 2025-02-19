# ========================================================
# Class Variables vs. Instance Variables
# ========================================================
# So far we've worked with both class variables and instance
# variables, but we haven't talked about the difference.
#
# Instance Variables
# ----------------
# Instance variables vary from object to object and are
# declared in the constructor.

class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20  # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"

# Class Variables
# -------------
# Class variables remain the same between instances of the
# same class and are declared at the top level of a class
# definition.

class Wall:
    height = 10

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20  # updates all instances of a Wall

print(south_wall.height)
# prints "20"

# In other languages these types of variables are often
# called static variables.
#
# Variables, Fields and Properties
# -----------------------------
# The terms instance and class variable, field, property
# and attribute are used interchangeably and usually refer
# to the same concept in languages that support some form
# of object-oriented programming. Here's a quick reference
# for some popular languages:
#
# Language    Class variable    Instance variable
# Python      Class variable    Instance variable
# Go          Field            Field
# JavaScript  Property         Property
# C#          Static field     Field
# Java        Static field     Field
#
# Which Should I Use?
# -----------------
# Generally speaking, stay away from class variables. Just
# like global variables, class variables are usually a bad
# idea because they make it hard to keep track of which
# parts of your program are making updates. However, it is
# important to understand how they work because you may see
# them out in the wild.
#
# Assignment
# ---------
# Some lazy code that's managed by another development team
# is causing some bugs in our team's class. We can fix it
# by using instance variables instead of class variables.
#
# In the main() function (that our team isn't responsible
# for), a line like Dragon.element = "fire" should not
# affect our existing dragon instances! We want our users
# to specify each dragon's element type when they create a
# new dragon with the constructor.
#
# Update the Dragon class. Remove the element class variable
# and instead use an instance variable that's configurable
# via the constructor.

class Dragon:

    def __init__(self, element):
        self.element = element

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


# don't touch below this line


def main():
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()