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
    # Constructor initializes a new bank account with an account number and starting balance
    # Double underscore creates private attributes for data protection
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private attribute to prevent direct modification
        self.__balance = initial_balance       # Private attribute to protect balance from tampering

    # Getter method to safely access the private account number
    # Provides read-only access to the account number
    def get_account_number(self):
        return self.__account_number

    # Getter method to safely access the private balance
    # Allows checking balance without exposing the private attribute
    def get_balance(self):
        return self.__balance

    # Method to add funds to the account
    # Validates input to ensure banking rules are followed
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")  # Ensures valid deposit amount
        self.__balance += amount  # Updates balance only if amount is valid

    # Method to remove funds from the account
    # Includes multiple validations to ensure safe transactions
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")  # Ensures valid withdrawal amount
        if amount > self.__balance:
            raise ValueError("insufficient funds")  # Prevents overdrawing the account
        self.__balance -= amount  # Updates balance only if all validations pass