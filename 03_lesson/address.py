class Address:
    index = "000000"
    city = "name"
    street = "name"
    house = "000"
    flat = "000"

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return (f"{self.index}, {self.city},"
        f"{self.street}, {self.house}"
        f"{self.flat}")