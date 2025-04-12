

class Country:
    def __init__(self,name, region):
        """
        Initialize the Country object with name and region.
        """
        self.name = name # name of the country
        self.region = region # region of the country
    
    def get_country_details(self):
        """
        Return a dictionary containing country details.
        """

        return {
            "Country name" : self.name,
            "Region" : self.region
        }
    
## Create a Country object
country = Country(name="India", region="Asia")

# Get country details
country_details = country.get_country_details()
for key, value in country_details.items():
    print(f"{key}: {value}")
