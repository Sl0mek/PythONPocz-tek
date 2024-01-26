from Shop.Order import Order
from Shop.Product import Product
from Shop.OrderElement import OrderElement

if __name__ == '__main__':
    order_elements = [OrderElement(product=Product(name="Procesor", category_name="Computer", unite_price=1000), quantity=1)]
    order = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    order.print()
    order.generate_order()
    order.print()
    print(order)