

class UserAccount:
    def __init__(self,cid, balance= 0.0):
        """
        Initialize the UserAccount object with customer ID and Balance
        """
        self.cid = cid # Customer ID
        self.balance = balance # Account Balance

    def get_account_details(self):
        """
        Returns a dictionary containing account details.
        """

        return {
            "Customer ID" : self.cid,
            "Balance" : self.balance
        }
    
    def deposit(self, amount):
        """
        Deposit amount into the account.
        """
        if amount > 0:
            self.balance += amount
            return f"{amount} Deposited Successfully. New Balance: {self.balance}"
        return "Invalid deposit amount!."
    
    def withdraw(self, amount):
        """
        withdraw amount from the account.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn Successfully. New Balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient Balance!"
        return "Invalid withdraw amount!"

## create a UserAccount object

user_account = UserAccount(
    cid = "CID123456",
    balance = 10000 # initial balance
)

## get account details
account_details = user_account.get_account_details()
for key,value in account_details.items():
    print(f"{key} : {value}")

## deposit amount
print(user_account.deposit(5000))
## withdraw amount
print(user_account.withdraw(3000))
## Attempt to withdraw more than balance
print(user_account.withdraw(15000))    

