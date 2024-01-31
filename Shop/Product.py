from dataclasses import dataclass
from Shop.ProductCategory import ProductCategory

@dataclass
class Product:
    name: str
    identifier: str
    category_name: ProductCategory
    unite_price: float

    def print(self):
        print(f"Name: {self.name}, Category: {self.category_name}, Unit price: {self.unite_price}")

    def __str__(self):
        return f"Name: {self.name}, Category: {self.category_name}, Unit price: {self.unite_price}"

    def __eq__(self, other):
        return self.name == other.name and self.category_name == other.category_name and self.unite_price == other.unite_price
