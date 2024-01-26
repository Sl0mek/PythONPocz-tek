from Shop.Product import Product


class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_price(self):
        return self.product.unite_price * self.quantity

    def print(self):
        print(f"{self.product}, Quantity {self.quantity}")

    def __str__(self):
        return f"{self.product}, Quantity {self.quantity}"

