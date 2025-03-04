"""
===================
Caravan
===================

Siege weapons (battering rams, catapults, etc.) are special units in Age of Dragons. Let's write the logic for how they move around the map.

===================
Challenge
===================

Complete the Siege, BatteringRam, and Catapult classes.

-------------------
Siege Class
-------------------
Complete the constructor. It accepts two parameters (in order) and sets them as instance variables with the same name:
    * Set max_speed
    * Set efficiency

Complete the get_trip_cost() method. It calculates the cost of a trip and returns it. The formula for calculating the cost is:

(distance / efficiency) * food_price

It costs food to move siege weapons, those things are heavy!

Leave the get_cargo_volume() method as empty. Use the pass keyword. Child classes will override this method.

-------------------
BatteringRam Class
-------------------
* Complete the constructor. It calls the parent constructor, then sets the extra battering-ram-only instance variables as member variables.
* The get_trip_cost() method uses the parent method to calculate the cost of food for a trip, plus the extra cost of carrying a load. The formula for calculating the cost:

base_cost + (load_weight * 0.01)

* The get_cargo_volume() method calculates and returns the cargo capacity in cubic meters. To get the volume of the battering-ram's 'bed' (cargo area), multiply its area by its depth, which is always 2 meters.

-------------------
Catapult Class
-------------------
* The constructor calls the parent constructor, then sets the extra catapult-only instance variable as a member variable.
* Do not override the get_trip_cost() method. It's inherited from the parent class.
* The get_cargo_volume() method just returns the cargo capacity of the catapult. This is already set by the constructor.
"""

class Siege:
    # Base efficiency calculations are separated into a parent class to allow
    # for future siege weapon types without duplicating core movement logic
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        # Food cost scales with efficiency to represent the mechanical complexity
        # of different siege weapons - more complex ones require more maintenance
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        # Abstract method to enforce cargo calculation implementation in child classes
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        # Additional weight penalty factor of 0.01 balances gameplay economy
        # without making rams prohibitively expensive to move
        return super().get_trip_cost(distance, food_price) + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        # Fixed depth of 2 meters chosen for gameplay balance and historical accuracy
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        # Catapults use fixed cargo volume since their design doesn't allow
        # for variable storage space like rams do
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
