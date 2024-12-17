"""
=========
DRY code
=========
Another "rule of thumb" for writing maintainable code is "Don't Repeat Yourself" (DRY). 
It just means that, when possible, you should avoid writing the same code in multiple places. 
Repeating code can be bad because:

    If you need to change it, you have to change it in multiple places
    If you forget to change it in one place, you'll have a bug
    It's more work to write it over and over again

----------
Assignment
----------
Your manager noticed that there's a lot of repetitive code in the "Age of Dragons" code base. 
She asked you to update the fight_soldiers function so that the DPS (damage-per-second) calculation is only written once.

Notice how these two lines are practically identical:

soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

Create a new function called get_soldier_dps that takes a soldier and 
returns its DPS using the same logic as the lines above. 
Then, replace the two lines above with calls to get_soldier_dps.
"""

# Function to simulate a fight between two soldiers based on their DPS
def fight_soldiers(soldier_one, soldier_two):
    # Calculate DPS for both soldiers using the helper function
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    
    # Compare DPS to determine the winner
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    # If DPS is equal, both soldiers die
    return "both soldiers die"

# Helper function to calculate a soldier's damage per second (DPS)
def get_soldier_dps(soldier):
    # Multiply damage by attacks per second to get total DPS
    return soldier["damage"] * soldier["attacks_per_second"]
