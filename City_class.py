from State_class import state
from Country_class import country

class City:
    def __init__(self, name, state):
        """
        Initialize the City object with name and associated state.
        """
        self.name = name  # Name of the city
        self.state = state  # Associated State object

    def get_city_details(self):
        """
        Return a dictionary containing city details.
        """
        return {
            "City Name": self.name,
            "State": self.state.name,
            "Country": self.state.country.name
        }

## Create a City object
city = City(name="Bangalore", state=state)


## Get city details
print("\nCity Details:")
city_details = city.get_city_details()
for key, value in city_details.items():
    print(f"{key}: {value}")