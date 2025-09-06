from address import Address

class Mailing:
    to_address = Address
    from_address = Address
    cost = "3344,55"
    track = "tr 16523456"

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def to_address(self):
        print(self.to_address)

    def from_adress(self):
        print(self.from_address)

