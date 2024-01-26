from Shop.Product import Product


class TaxCalculator:

    FRUITS_AND_VEGETABLES = 5
    FOOD = 8
    OTHER = 20

    @classmethod
    def calculateTax(cls, product):
        if product.category_name == "Fruits and vegetables":
            return product.unite_price * 0.05
        elif product.category_name == "Food":
            return product.unite_price * 0.08
        else:
            return product.unite_price * 0.2
