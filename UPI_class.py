from Account_class import account
from userClass import user_Obj
from random import randint

class UPI:
    def __init__(self,upi_id,cid):
        self.upi_id = upi_id
        self.cid = cid
        self.linked_account = []
        self.__upi_extension = ["@upi"] #default upi extension

    def generate_upi_id(self):
        """
        Generate a unique UPI ID.
        
        """
        __upi = f"{self.cid}@{self.generate_upi_id[randint(0,len(self.__upi_extension)-1)]}"
        return __upi

    def link_account(self, account):
        """
        Link an account to the UPI ID.
        
        """
        if account not in self.linked_account:
            self.linked_account.append(account)
            return f"Account {account} linked successfully."
        return f"Account {account} is already linked."
    
    def unlink_account(self,account):
        """
        unlink an account from the UPI ID

        """
        if account in self.linked_account:
            self.linked_account.remove(account)
            return f"Account {account} unlinked successfully."
        return f"Account {account} is not linked."
    
    def get_linked_accounts(self):
        """
        return the list of linked accounts

        """
        return self.linked_account
    
    def validate_transaction(self, amount, account):
        """
        validate if a transaction can be made with the linked accounts

        """
        if account in self.linked_account:
            if amount > 0:
                return f"Transaction of {amount} is valid for account {account}."
            return "Invalid transaction amount!"
        return f"Account {account} is not linked to the UPI ID {self.upi_id}."
    
## Account obj

account_obj = account("admin", "password123")

## creating UPI object
UPI_Obj = UPI("user@upi", account_obj.cid())

## link accounts 

print(UPI_Obj.link_account("Account001"))
print(UPI_Obj.link_account("Account002"))

## Get linked accounts
print("linked accounts:", UPI_Obj.get_linked_accounts())

## validat a transaction
print(UPI_Obj.validate_transaction(5000, "Account001"))


## unlink an account
print(UPI_Obj.unlink_account("Account001"))

## Validate a transaction after unlinked account
print(UPI_Obj.validate_transaction(5000, "Account001"))

