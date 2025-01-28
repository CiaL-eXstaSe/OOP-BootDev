"""
==================
Methods vs Functions
==================
You know what a function is. A method has all the same properties as a function, 
but it is tied directly to a class and has access to all its properties.

A method automatically receives the object it was called on as its first parameter.
"""

class Soldier:
    health = 5

    def take_damage(self, damage, multiplier):
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
damage, multiplier = 30, 3

# Only "damage" and "multiplier" are passed as arguments
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(damage, multiplier)

"""
-----------------
Method Properties
-----------------
A method can operate on data that is contained within the class. In other words, you won't always see all the "outputs" 
in the return statement because the method might just mutate the object's properties directly.

--------------
The OOP Debate 
--------------
Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. 
In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.

For example, while methods are more implicit and often make code more difficult to read, they also make it easier to group 
a program's data and behavior in one place, which can lead to a more organized codebase.
"""
