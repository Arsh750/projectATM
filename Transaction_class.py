import json
from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, cid, transaction_type, transaction_amount, remarks, storage_file="transactions.json"):
        self.transaction_id = transaction_id
        self.cid = cid
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.remarks = remarks
        self.transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.storage_file = storage_file
        self.save_transaction()

    def save_transaction(self):
        try:
            with open(self.storage_file, "r") as file:
                transactions = json.load(file)
        except FileNotFoundError:
            transactions = []
        transactions.append({
            "transaction_id": self.transaction_id,
            "cid": self.cid,
            "transaction_type": self.transaction_type,
            "transaction_amount": self.transaction_amount,
            "remarks": self.remarks,
            "transaction_time": self.transaction_time,
        })
        with open(self.storage_file, "w") as file:
            json.dump(transactions, file, indent=4)