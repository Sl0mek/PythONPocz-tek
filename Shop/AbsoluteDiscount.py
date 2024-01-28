from Shop.DiscountPolicy import DiscountPolicy


class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, value):
        self._value = value

    def apply_discount(self, amount):
        amount -= self._value
        if amount < 0:
            return 0
        else:
            return amount
