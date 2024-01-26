class DiscountPolicy:

    @classmethod
    def loyal_customer_policy(cls, total_price):
        return total_price * 0.95

    @classmethod
    def christmas_policy(cls, total_price):
        if total_price > 100:
            total_price -= 20
        return total_price