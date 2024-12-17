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

# Define a Wall class with properties and a method to strengthen it
class Wall:
    # Initial properties
    armor = 10    # Base armor value
    height = 5    # Base height value

    # Method to strengthen the wall by doubling its armor
    def fortify(self):
        # Multiply the current armor by 2
        self.armor *= 2

# Create a wall instance and test the fortify method
wall = Wall()
# Call the fortify method to double the wall's armor
wall.fortify()
# Print the new armor value (should be 20)
print(wall.armor)