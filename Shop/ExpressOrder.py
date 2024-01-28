from Shop.Order import Order


class ExpressOrder(Order):

    FEE = 100

    def __init__(self, customer_first_name, customer_last_name, delivery_time, order_elements=None, discount_policy=None):
        super().__init__(customer_first_name=customer_first_name,
                        customer_last_name=customer_last_name,
                        order_elements=order_elements,
                        discount_policy=discount_policy)

        self._delivery_time = delivery_time


    @property
    def delivery_time(self):
        return self._delivery_time

    def _calculate_total_prize(self):
        return super()._calculate_total_prize() + ExpressOrder.FEE

    def __str__(self):
        order = (20 * "=") + "\n"
        order += f"Customer: {self._customer_first_name} {self._customer_last_name}\n"
        order += f"Total price {self._calculate_total_prize()}\n"
        if self._order_elements:
            for order_element in self._order_elements:
                order += str(order_element) + "\n"
        else:
            return "Order is empty!"
        order += f"Delivery time: {self._delivery_time}\n"
        order += (20 * "=") + "\n"
        return order





