import json

class Cards:
    def __init__(self, card_id, card_type, status="Active", storage_file="cards.json"):
        self.card_id = card_id
        self.card_type = card_type
        self.status = status
        self.storage_file = storage_file
        self.save_card()

    def save_card(self):
        try:
            with open(self.storage_file, "r") as file:
                cards = json.load(file)
        except FileNotFoundError:
            cards = []
        cards.append({
            "card_id": self.card_id,
            "card_type": self.card_type,
            "status": self.status,
        })
        with open(self.storage_file, "w") as file:
            json.dump(cards, file, indent=4)
    def activate_card(self):
        """
        Activate the card by setting its status to 'Active'.
        """
        self.status = "Active"
        self.save_card()
        return f"Card {self.card_id} has been activated."

    def deactivate_card(self):
        """
        Deactivate the card by setting its status to 'Inactive'.
        """
        self.status = "Inactive"
        self.save_card()
        return f"Card {self.card_id} has been deactivated."