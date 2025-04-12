from datetime import datetime, timedelta

class UserTransaction:
    def __init__(self, transaction_id, cid,transaction_time = None):
        """
        Inittialize the UserTransaction object with transaction details.
        """
        self.transaction_id = transaction_id # unique identifier for the transaction
        self.cid = cid # Customer ID associated with the transaction
        self.transaction_time = transaction_time or datetime.now() # Timestamp of when the transaction occurred


    def get_user_transaction(self):
        """
        Returns a dictionary containing user transaction details.
        """

        return {
            "Transaction ID" : self.transaction_id,
            "Customer ID" : self.cid,
            "Transaction Time" : self.transaction_time.strftime("%Y-%m-%d %H:%M:%S")

        }
    
    def is_recent_transaction(self, minutes = 5):
        """
        Check if the transaction occurred within the last 'minutes'.
        """
        time_difference = datetime.now() -self.transaction_time
        return time_difference.total_seconds() <= minutes * 60
    

## create a UserTransaction object
user_transaction = UserTransaction(
    transaction_id = "TXN123456",
    cid = "CID123456",
    transaction_time = datetime.now() - timedelta(minutes = 3) # simulating a recent transaction
)

## get user transaction details
transaction_details = user_transaction.get_user_transaction()
for key,value in transaction_details.items():
    print(f"{key} : {value}")

## check if the transaction is recent
is_recent = user_transaction.is_recent_transaction(minutes = 5)
print(f"Is the transaction recent? {'yes' if is_recent else 'no'}")
