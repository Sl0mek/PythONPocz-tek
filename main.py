from Shop.Order import Order
from Shop.Product import Product
from Shop.OrderElement import OrderElement
from Shop.DiscountPolicy import DiscountPolicy

def joinArgs(*args):
    tmp = ""
    for arg in args:
        tmp += str(arg) + "-"
    return tmp

def joinKwargs(**kwargs):
    tmp = ""
    for arg in kwargs:
        tmp += str(arg) + "=" + str(kwargs[arg]) + ","
    return tmp

def unpackingExample():
    list1 = [3, 4, 1]
    list2 = [6, 8, 33]
    combined_numbers = [*list1, *list2]
    print(combined_numbers)

    dict1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    dict2 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    combined_dict = {**dict1, **dict2}
    print(combined_dict)


if __name__ == '__main__':
    order_elements = [OrderElement(product=Product(name="Procesor", category_name="Computer", unite_price=1000), quantity=1),
                      OrderElement(product=Product(name="Graphic card", category_name="Computer", unite_price=1200), quantity=1),
                      OrderElement(product=Product(name="RAM", category_name="Computer", unite_price=700), quantity=1),
                      OrderElement(product=Product(name="Disc", category_name="Computer", unite_price=200), quantity=1),
                      OrderElement(product=Product(name="Power suply", category_name="Computer", unite_price=300), quantity=1),
                      OrderElement(product=Product(name="Cooling", category_name="Computer", unite_price=100), quantity=1)]
    order1 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements, discount_policy=DiscountPolicy.christmas_policy)
    order1.print()
    order1.sort_elements()
    order1.print()
    order1.generate_order(100)
    order1.print()
    print(order1)
    order2 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    print(order1 == order2)
    order2.add_new_order_element(name="Procesor", category_name="Computer", unite_price=1000, quantity=2)
    print(order2)

    print(joinArgs(1, 2, 3, 4, 5))
    print(joinKwargs(andrzej="słomka", jan="Kowalski"))

    unpackingExample()