"""
==================
The Calculator
==================

Assignment
----------
Complete the Calculator class.

Constructor
----------
Create a private instance variable called result initialized to 0.

Math
----------
The following methods should perform their respective mathematic computations. 
The "left-hand side" of each operation should be the current value of the result variable. 
The "right-hand side" of each operation will be the value passed in.

    * add(self, a)
    * subtract(self, a)
    * multiply(self, a)
    * divide(self, a): If the user attempts to divide by 0, raise a ValueError 
      with "cannot divide by zero" as the argument
    * modulo(self, a): If the user attempts to divide by 0, raise a ValueError 
      with "cannot divide by zero" as the argument
    * power(self, a)
    * square_root(self)

Helper Methods
----------
    * clear(self): reset the result variable to 0
    * get_result(self): return the current value stored in the calculator's 
      private result variable.

Hints
----------
    * For the power and square_root operations, search your spellbook for how 
      to use exponents in Python.
    * To calculate the square root of a number you can raise it to the power of 0.5.
"""

class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("cannot divide by zero")
        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("cannot divide by zero")
        self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result