from Country_class import country
class State:
    def __init__(self, name, country):
        """
        Initialize the State object with name and associated country.
        """
        self.name = name  # Name of the state
        self.country = country  # Associated Country object

    def get_state_details(self):
        """
        Return a dictionary containing state details.
        """
        return {
            "State Name": self.name,
            "Country": self.country.name
        }
    


## Create a State object
state = State(name="Madhya Pradesh", country=country)

## Get state details
print("\nState Details:")
state_details = state.get_state_details()
for key, value in state_details.items():
    print(f"{key}: {value}")