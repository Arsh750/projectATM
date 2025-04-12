import json

class account:
    def __init__(self, username, password, storage_file="accounts.json"):
        self.username = username
        self.password = password
        self.storage_file = storage_file
        self.load_account()

    def load_account(self):
        try:
            with open(self.storage_file, "r") as file:
                accounts = json.load(file)
                account_data = accounts.get(self.username, {})
                self.balance = account_data.get("balance", 0.0)
                self.status = account_data.get("status", "Active")
                self.cards = account_data.get("cards", [])
        except FileNotFoundError:
            self.balance = 0.0
            self.status = "Active"
            self.cards = []

    def save_account(self):
        try:
            with open(self.storage_file, "r") as file:
                accounts = json.load(file)
        except FileNotFoundError:
            accounts = {}
        accounts[self.username] = {
            "balance": self.balance,
            "status": self.status,
            "cards": self.cards,
        }
        with open(self.storage_file, "w") as file:
            json.dump(accounts, file, indent=4)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save_account()
            return f"₹{amount} deposited successfully. New balance: ₹{self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.save_account()
            return f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}"
        elif amount > self.balance:
            return "Insufficient balance!"
        return "Invalid withdrawal amount!"