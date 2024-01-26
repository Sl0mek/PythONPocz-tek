from Shop.Order import Order
from Shop.Product import Product
from Shop.OrderElement import OrderElement

if __name__ == '__main__':
    order_elements = [OrderElement(product=Product(name="Procesor", category_name="Computer", unite_price=1000), quantity=1),
                      OrderElement(product=Product(name="Graphic card", category_name="Computer", unite_price=1200), quantity=1),
                      OrderElement(product=Product(name="RAM", category_name="Computer", unite_price=700), quantity=1),
                      OrderElement(product=Product(name="Disc", category_name="Computer", unite_price=200), quantity=1),
                      OrderElement(product=Product(name="Power suply", category_name="Computer", unite_price=300), quantity=1),
                      OrderElement(product=Product(name="Cooling", category_name="Computer", unite_price=100), quantity=1)]
    order1 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    order1.print()
    order1.generate_order(100)
    order1.print()
    print(order1)
    order2 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    print(order1 == order2)
    order2.add_new_order_element(name="Procesor", category_name="Computer", unite_price=1000, quantity=2)
    print(order2)