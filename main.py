from Shop.Order import Order
from Shop.Product import Product
from Shop.OrderElement import OrderElement

if __name__ == '__main__':
    order_elements = [OrderElement(product=Product(name="Procesor", category_name="Computer", unite_price=1000), quantity=1)]
    order1 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    order1.print()
    order1.generate_order()
    order1.print()
    print(order1)
    order2 = Order(customer_first_name="Jan", customer_last_name="Slomka", order_elements=order_elements)

    print(order1 == order2)