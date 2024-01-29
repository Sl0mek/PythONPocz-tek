from Shop.OrderElement import OrderElement, Product
import random

class DataGenerator:
    MAX_ORDER_ELEMENTS = 5

    @classmethod
    def generate_base_order(cls):
        return [OrderElement(product=Product(name="Procesor", identifier="1", category_name="Computer", unite_price=1000), quantity=1),
                OrderElement(product=Product(name="Graphic card", identifier="2", category_name="Computer", unite_price=1200),
                             quantity=1),
                OrderElement(product=Product(name="RAM", identifier="23", category_name="Computer", unite_price=700), quantity=1),
                OrderElement(product=Product(name="Disc", identifier="12", category_name="Computer", unite_price=200), quantity=1),
                OrderElement(product=Product(name="Power suply", identifier="332", category_name="Computer", unite_price=300),
                             quantity=1),
                OrderElement(product=Product(name="Cooling", identifier="2656", category_name="Computer", unite_price=100), quantity=1)]

    @classmethod
    def generate_rnd_order(cls, quantity=None):
        order_elements = []
        if not quantity:
            quantity = random.randint(1, cls.MAX_ORDER_ELEMENTS)
        if quantity > cls.MAX_ORDER_ELEMENTS:
            quantity = cls.MAX_ORDER_ELEMENTS
        for i in range(1, quantity + 1):
            order_elements.append(
                OrderElement(Product(name=f"Product {i}", identifier=f"ID {i}", category_name=f"Category {i}", unite_price=i), quantity=i))
        return order_elements
