#!/usr/bin/python3

class Checkbook:
    """Simple checkbook with deposit, withdraw, and balance operations."""

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def get_positive_amount(prompt):
    """Ask the user for a positive number until a valid value is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    cb = Checkbook()
    while True:
        action = input("Choose action (deposit, withdraw, balance, exit): ").lower()
        if action == "exit":
            print("Goodbye!")
            break
        elif action == "deposit":
            amount = get_positive_amount("Amount to deposit: $")
            cb.deposit(amount)
        elif action == "withdraw":
            amount = get_positive_amount("Amount to withdraw: $")
            cb.withdraw(amount)
        elif action == "balance":
            cb.get_balance()
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
