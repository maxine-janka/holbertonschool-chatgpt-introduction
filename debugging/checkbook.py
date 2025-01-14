#!/usr/bin/python3
"""
Checkbook Module

This module provides a simple checkbook application that allows users to manage their account balance by performing deposits, withdrawals, and viewing the current balance. It is implemented using a `Checkbook` class and an interactive command-line interface.

Classes:
    Checkbook: Represents a checkbook account with functionality to deposit, withdraw, and check the balance.

Functions:
    main(): Runs the command-line interface for the checkbook application.

Usage:
    Run the module directly to use the checkbook application interactively.
"""

class Checkbook:
    """
    A class to represent a checkbook account.

    Attributes:
        balance (float): The current account balance, initialized to 0.0.

    Methods:
        deposit(amount): Adds the specified amount to the balance.
        withdraw(amount): Deducts the specified amount from the balance if sufficient funds exist.
        get_balance(): Prints the current balance.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit into the account.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if sufficient funds exist.
        Prints a warning if the balance is insufficient.

        Args:
            amount (float): The amount to withdraw from the account.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current account balance.

        Args:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Runs the command-line interface for the checkbook application.

    Users can perform the following actions:
        - deposit: Add funds to the account.
        - withdraw: Remove funds from the account.
        - balance: View the current account balance.
        - exit: Exit the application.

    The application continuously prompts the user until they choose to exit.

    Args:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
