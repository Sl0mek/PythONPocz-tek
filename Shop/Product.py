class Product:

    def __init__(self, name, category_name, unite_price):
        self.name = name
        self.category_name = category_name
        self.unite_price = unite_price

    def print(self):
        print(f"Name: {self.name}, Category: {self.category_name}, Price: {self.unite_price}")

