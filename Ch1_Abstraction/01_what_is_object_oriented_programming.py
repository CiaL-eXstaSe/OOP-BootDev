"""
What is object-oriented programming?

Object-Oriented Programming, or "OOP", is a pattern for writing clean and maintainable code. 
Not everyone agrees that object-oriented principles are the best way to write code, but, 
to be a good engineer, you should at least understand them.

In this course, we'll be coding the pieces of a real-time strategy game called "Age of Dragons". 
Players control armies of people, elves, orcs, and dragons and battle each other. 
It's similar to Age of Empires or StarCraft.

-----------
Assignment
-----------
One of the greatest sins when trying to write "clean code" is using misleading names for your variables and functions. 
Take a look at the destroy_wall function. 
Based on its name, you might assume that it destroys a single wall, 
but if you look closely, you'll see that it handles multiple walls.

The test suite expects a different function name. 
Take a look at the main_test.py file to see what it's looking for, 
and rename the function accordingly.

Additionally, try to rename the variables inside the function to be more descriptive. 
After passing the tests, take a look at the solution to see how we named everything.
"""
def destroy_walls(wall_healths):
    for wall_health in wall_healths:
        if wall_health <= 0:
            wall_healths.remove(wall_health)
    return wall_healths
