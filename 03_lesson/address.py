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

    def print_index(self):
        print("index:", self.index)

    def print_city(self):
        print("city:", self.city)

    def print_street(self):
        print("street:", self.street)

    def print_house(self):
        print("house:", self.house)

    def print_flat(self):
        print("flat:", self.flat)