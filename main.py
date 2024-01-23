from Shop.Order import Order
from Shop.Product import Product

if __name__ == '__main__':
    product1 = Product(name="Procesor", category_name="Computer", unite_price=1000)
    products = [product1]
    order = Order(customer_first_name="Andrzej", customer_last_name="Slomka", products=products)
    order.print()
    order.generate_order()
    order.print()