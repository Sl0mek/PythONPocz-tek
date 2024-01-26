import random
from Shop.Product import Product
from Shop.OrderElement import OrderElement


class Order:

    MAX_ORDER_ELEMENTS  = 5

    def __init__(self, customer_first_name, customer_last_name, order_elements=None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        if order_elements is None:
            self._order_elements = []
        else:
            if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
                self._order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
            else:
                self._order_elements = order_elements

    def print(self):
        print(20 * "=")
        print(f"Customer: {self.customer_first_name} {self.customer_last_name}")
        print(f"Total price {self._calculate_total_prize()}")
        if self._order_elements:
            for order_element in self._order_elements:
                order_element.print()
        else:
            print("Order is empty!")
        print(20 * "=")

    def generate_order(self, quantity):
        if quantity > Order.MAX_ORDER_ELEMENTS:
            quantity = Order.MAX_ORDER_ELEMENTS
        self._order_elements.clear()
        for i in range(1, quantity):
            self._order_elements.append(
                OrderElement(Product(name=f"Product {i}", category_name=f"Category {i}", unite_price=i), quantity=i))

    def _calculate_total_prize(self):
        sum = 0
        for order_element in self._order_elements:
            sum += order_element.calculate_price()
        return sum

    def add_new_order_element(self, name, category_name, unite_price, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            self._order_elements.append(OrderElement(product=Product(name=name, category_name=category_name, unite_price=unite_price), quantity=quantity))
        else:
            print("To much elements in order")

    def __str__(self):
        order = (20 * "=") + "\n"
        order += f"Customer: {self.customer_first_name} {self.customer_last_name}\n"
        order += f"Total price {self._calculate_total_prize()}\n"
        if self._order_elements:
            for order_element in self._order_elements:
                order += str(order_element) + "\n"
        else:
            return "Order is empty!"
        order += (20 * "=") + "\n"
        return order

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if not self.customer_first_name == other.customer_first_name and self.customer_last_name == other.customer_last_name:
            return False
        for order_element in self._order_elements:
             if not order_element in other._order_elements:
                 return False
        return True
