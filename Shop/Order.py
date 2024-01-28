import random
from Shop.Product import Product
from Shop.OrderElement import OrderElement


class Order:

    MAX_ORDER_ELEMENTS = 6

    def __init__(self, customer_first_name, customer_last_name, order_elements=None, discount_policy=None):
        self._customer_first_name = customer_first_name
        self._customer_last_name = customer_last_name
        self._discount_policy = discount_policy
        if order_elements is None:
            self._order_elements = []
        else:
            if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
                self._order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]
            else:
                self._order_elements = order_elements

    def print(self):
        print(20 * "=")
        print(f"Customer: {self._customer_first_name} {self._customer_last_name}")
        print(f"Total price {self._calculate_total_prize()}")
        if self._order_elements:
            for order_element in self._order_elements:
                order_element.print()
        else:
            print("Order is empty!")
        print(20 * "=")

    @property
    def customer_first_name(self):
        return self._customer_first_name

    @property
    def customer_last_name(self):
        return self._customer_last_name

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, var):
        if len(var) > Order.MAX_ORDER_ELEMENTS:
            self._order_elements = var[:Order.MAX_ORDER_ELEMENTS]
        else:
            self._order_elements = var

    @property
    def total_price(self):
        return self._calculate_total_prize()

    def _calculate_total_prize(self):
        sum = 0
        for order_element in self._order_elements:
            sum += order_element.calculate_price()
        if self._discount_policy:
            sum = self._discount_policy.apply_discount(sum)
        return sum

    def add_new_order_element(self, name, category_name, unite_price, quantity):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            self._order_elements.append(OrderElement(product=Product(name=name, category_name=category_name, unite_price=unite_price), quantity=quantity))
        else:
            print("To much elements in order")

    def _sort_price(self, order_element):
        return order_element.calculate_price()

    def sort_elements(self, pred = None):
        if pred:
            self._order_elements.sort(key=pred)
        else:
            # self._order_elements.sort(key=self._sort_price)
            self._order_elements.sort(key=lambda order_element: order_element.calculate_price())

    def __str__(self):
        order = (20 * "=") + "\n"
        order += f"Customer: {self._customer_first_name} {self._customer_last_name}\n"
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
        if not self._customer_first_name == other.customer_first_name and self._customer_last_name == other.customer_last_name:
            return False
        for order_element in self._order_elements:
             if not order_element in other.order_elements:
                 return False
        return True
