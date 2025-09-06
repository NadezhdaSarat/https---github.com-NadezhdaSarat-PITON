class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def print_brand(self):
        print("brand:", self.brand)

    def print_model(self):
        print("model:", self.model)

    def print_phone_number(self):
        print("phone_number:", self.phone_number)