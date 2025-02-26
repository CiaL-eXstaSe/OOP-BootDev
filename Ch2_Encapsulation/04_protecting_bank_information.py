"""
===============================
Protecting Bank Information
===============================

Description:
-----------
Age of Dragons is a game about resource management and strategy. The game has a 
feature that allows players to manage their resources in a bank. The bank has a 
feature that allows players to deposit and withdraw funds.

Assignment Requirements:
----------------------
Complete the BankAccount class with the following:

Constructor:
-----------
- Set __account_number to account_number
- Set __balance to initial_balance

Public Getters:
--------------
- get_account_number(): Returns private __account_number
- get_balance(): Returns private __balance

Deposit Method:
-------------
- Accepts amount parameter
- Validates amount is positive
- Raises ValueError if amount <= 0 with message:
  "cannot deposit zero or negative funds"
- Adds amount to balance if valid

Withdraw Method:
--------------
- Accepts amount parameter
- Validates amount is positive
- Validates sufficient funds available
- Raises ValueError if amount <= 0 with message:
  "cannot withdraw zero or negative funds"
- Raises ValueError if insufficient funds with message:
  "insufficient funds"
- Deducts amount from balance if valid
"""

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount