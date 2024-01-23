import random
from Shop.Product import Product

class Order:

    def __init__(self, customer_first_name, customer_last_name, products = None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        if products is None:
            self.products = []
        else:
            self.products = products
        self.total_price = 0
        for product in products:
            self.total_price = self.total_price + product.unite_price

    def print(self):
        print(20 * "=")
        print(f"Customer: {self.customer_first_name} {self.customer_last_name}")
        print(f"Total price {self.total_price}")
        if self.products:
            for product in self.products:
                product.print()
        else:
            print("Order is empty!")
        print(20 * "=")

    def generate_order(self):
        number = random.randint(1, 10)
        self.products.clear()
        for i in range(1, number):
            self.products.append(Product(name=f"Product {i}", category_name=f"Category {i}", unite_price=i))
