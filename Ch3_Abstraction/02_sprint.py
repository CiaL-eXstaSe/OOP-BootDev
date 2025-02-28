"""
===================
Sprint
===================

In the game we're making, Age of Dragons, humans can "sprint" allowing them 
to move twice as fast. However, sprinting requires stamina. Each time a human 
sprints, it loses stamina. Once it is out of stamina, it can no longer sprint.

===================
Assignment
===================

Complete all of the missing methods.

The __raise_if_cannot_sprint() and __use_sprint_stamina() are private methods 
that are only intended to be used within the class. In your case, you'll use 
them to build the other four sprinting methods.

-------------------
__raise_if_cannot_sprint()
-------------------
This method should raise the exception: not enough stamina to sprint if the 
human is out of stamina.

-------------------
__use_sprint_stamina()
-------------------
Remove one stamina from the human.

-------------------
For Each of the Remaining Methods:
-------------------
* Raise an error if there isn't enough stamina to sprint 
  (use __raise_if_cannot_sprint())
* Use the stamina needed to sprint (use __use_sprint_stamina())
* Move twice in the direction of the sprint.
"""

class Human:
    # Sprint methods follow a consistent pattern:
    # 1. Check if sprinting is possible
    # 2. Consume stamina
    # 3. Move twice in the desired direction
    
    def sprint_right(self):
        # First verify we have enough stamina to sprint
        self.__raise_if_cannot_sprint()
        # Consume one stamina point for the sprint action
        self.__use_sprint_stamina()
        # Move twice using the existing move_right() method
        # Original implementation directly modified position:
        # self.__pos_x += self.__speed * 2
        # This is better than directly modifying position because:
        # - It reuses existing code (DRY principle)
        # - Any changes to movement logic will automatically apply to sprinting
        # - Maintains encapsulation of position variables
        self.move_right()
        self.move_right()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        # Same pattern as sprint_right, but using move_left()
        self.move_left()
        self.move_left()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        # Same pattern as other sprint methods
        self.move_up()
        self.move_up()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        # Same pattern as other sprint methods
        self.move_down()
        self.move_down()

    def __raise_if_cannot_sprint(self):
        # Private helper method to check sprint conditions
        # Throws an exception if stamina is depleted
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        # Private helper method to handle stamina consumption
        # Reduces stamina by 1 for each sprint action
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina