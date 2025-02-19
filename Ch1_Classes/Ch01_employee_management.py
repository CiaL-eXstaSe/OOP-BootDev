"""
===================
Employee Management
===================

Description
-----------
"Age of Dragons, Inc." is growing rapidly. They need a way to keep track of 
all their employees. This tool helps manage employee information.

Challenge Details
----------------
Design requirement: Use shared class variables to track company name and 
total employee count within the Employee class.

Class Structure
--------------
Class Variables:
- company_name: "Age of Dragons, Inc."
- total_employees: Counter starting at 0

Constructor Parameters:
- first_name
- last_name
- id
- position
- salary
Note: Increments total_employees on each new instance

Methods
-------
get_name():
- Returns: Employee's full name as string (format: "First Last")
"""

class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0
    
    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1
    
    def get_name(self):
        return f"{self.first_name} {self.last_name}"
