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

def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
