from Shop.Order import Order
from Shop.DiscountPolicy import DiscountPolicy
from Shop.DataGenerator import DataGenerator
from Shop.ExpressOrder import ExpressOrder
from Shop.PercentageDiscount import PercentageDiscount
from Shop.AbsoluteDiscount import AbsoluteDiscount
from Shop.OrderElementLimitException import OrderElementLimitException

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


def notationExample():
    tmp = input("Enter number:\n>")
    try:
        if tmp.isnumeric():
            output = ""
            for i, x in enumerate(tmp[::-1]):
                output += x
                if i % 3 == 2:
                    output += "_"
            output = output.strip("_")
            print(output[::-1])
            print(hex(int(tmp)))
            print(oct(int(tmp)))

        else:
            raise ValueError(f"Is not a number {tmp}")
    except ValueError as error:
        print(error)

def printNum(num):
    dig = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
        ]
    numStr = str(num)
    for i in range(5):
        for j in numStr:
            print(dig[int(j)][i] + " ", end="")
        print()


if __name__ == '__main__':
    printNum(9081726354)
    order_elements = DataGenerator.generate_base_order()
    order1 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements,
                   discount_policy=DiscountPolicy())
    order1.print()
    order1.sort_elements()
    order1.print()
    order1.order_elements = DataGenerator.generate_rnd_order(10)
    order1.print()
    print(order1)
    order2 = Order(customer_first_name="Andrzej", customer_last_name="Slomka", order_elements=order_elements)
    print(order1 == order2)

    try:
        order2.add_new_order_element(name="Procesor", category_name="Computer", unite_price=1000, quantity=2)
    except OrderElementLimitException as error:
        print(error)

    print(order2)
    express_order = ExpressOrder(customer_first_name="Andrzej", customer_last_name="Slomka", delivery_time="10.10.2024",
                                 order_elements=order_elements,
                                 discount_policy=PercentageDiscount(value=10))
    print(express_order)
    express_order = ExpressOrder(customer_first_name="Andrzej", customer_last_name="Slomka", delivery_time="10.10.2024",
                                 order_elements=order_elements,
                                 discount_policy=AbsoluteDiscount(value=3000))
    print(express_order)

    print(joinArgs(1, 2, 3, 4, 5))
    print(joinKwargs(andrzej="słomka", jan="Kowalski"))

    # unpackingExample()

    print({i: i for i in range(10)})

    notationExample()

    # from platform import platform
    #
    # print(platform())
    # print(platform(1))
    # print(platform(0, 1))

    from platform import python_implementation, python_version_tuple

    print(python_implementation())

    for atr in python_version_tuple():
        print(atr, end=".")
