from Shop.DiscountPolicy import DiscountPolicy


class PercentageDiscount(DiscountPolicy):

    def __init__(self, value):
        self._value = 1 - value/100

    def apply_discount(self, amount):
        return amount * self._value
