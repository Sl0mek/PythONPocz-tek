from Shop.Product import Product
from dataclasses import dataclass


@dataclass
class OrderElement:
    product: Product
    quantity: int

    def calculate_price(self):
        return self.product.unite_price * self.quantity

    def print(self):
        print(f"{self.product}, Quantity {self.quantity}")

    def __str__(self):
        return f"{self.product}, Quantity {self.quantity}"

    def __eq__(self, other):
        return self.product == other.product and self.quantity == other.quantity

    def __lt__(self, other):
        return self.calculate_price() < other.calculate_price()

    def __le__(self, other):
        return self.calculate_price() <= other.calculate_price()

    def __gt__(self, other):
        return self.calculate_price() > other.calculate_price()

    def __ge__(self, other):
        return self.calculate_price() >= other.calculate_price()
