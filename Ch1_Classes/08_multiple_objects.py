"""
=================
Multiple Objects
=================
An object is an "instance" of a class. Let's look at what that means.

    In object-oriented programming, an instance is a concrete occurrence of any object... 
    "Instance" is synonymous with "object" as they are each a particular value... 
    "Instance" emphasizes the distinct identity of the object. The creation of an instance 
    is called instantiation.

    -- Wikipedia

So for our wall class, I can create three different "instances" of the class. 
Or, in other words, I can create three separate objects.
"""

# wall_maria = Wall(1, 2, 3)
# wall_rose = Wall(4, 5, 6)
# wall_sina = Wall(9, 8, 7)

"""
In the example above, the variables are instances of the Wall type.

-----------
Assignment
-----------
Take a look at the Brawler class and the fight function provided.

In the main function:

    Create 4 new brawlers with the following stats:
        Name: Aragorn. Speed: 4. Strength: 4.
        Name: Gimli. Speed: 2. Strength: 7.
        Name: Legolas. Speed: 7. Strength: 7.
        Name: Frodo. Speed: 3. Strength: 2.
    
    Call fight twice:
        - The first fight should be Aragorn vs Gimli.
        - The second will be Legolas vs Frodo.
"""

def main():
    brawler_aragorn = Brawler(4, 4, "Aragorn")
    brawler_gimli = Brawler(2, 7, "Gimli")
    brawler_legolas = Brawler(7, 7, "Legolas")
    brawler_frodo = Brawler(3, 2, "Frodo")

    fight(brawler_aragorn, brawler_gimli)
    fight(brawler_legolas, brawler_frodo)


# don't touch below this line


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()