class user:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def cid(self):
        return f"CID: {abs(hash(self.username))}"

    def type(self):
        return f"Type: Regular User"

    def description(self):
        return f"user: {self.username} with password: {self.password}"

    def cif(self):
        return f"CIF: CIF123456"

    def ifsc(self):
        return f"IFSC: IFSC123456"

    def address(self):
        return f"Address: 123 main street, city, country"

    def created_at(self):
       from datetime import datetime
       return f"TimeStamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    def display_all(self):
        print(user_Obj.cid())
        print(user_Obj.type())
        print(user_Obj.description())
        print(user_Obj.cif())
        print(user_Obj.ifsc())
        print(user_Obj.address())
        print(user_Obj.created_at())
    

user_Obj = user("admin", "password123")
user_Obj.display_all()
