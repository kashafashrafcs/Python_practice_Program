class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount


account = BankAccount("Ali", 1000)

deposit_amount = int(input("Enter deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdraw amount: "))
account.withdraw(withdraw_amount)

print("Balance:", account.balance)

try:
    amount = int(input("Enter amount to withdraw again: "))
    account.withdraw(amount)
except InsufficientFundsError as e:
    print(f"Error: {e}")

print("Final balance:", account.balance)