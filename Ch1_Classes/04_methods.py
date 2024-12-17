"""
========
Methods
========
After the last exercise, you might be wondering why classes are useful, 
they're like dictionaries... but worse!

One thing that makes classes cool is that we can define methods on them. 
A method is a function that's tied directly to a class and has access to all its properties.

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

-----
Self
-----
Methods are nested within the class declaration. 
Their first parameter is always the instance of the class that the method is being called on.
By convention, it's called "self". Because self is a reference to the object, 
you can use it to read and update the properties of the object.

Notice that methods are called directly on an object using the dot operator.

my_object.my_method()

----------
Assignment
----------
Add a fortify() method to your wall class. 
It should double the current armor property.
"""

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2

wall = Wall()
wall.fortify()
print(wall.armor)