from Shop.Product import Product


class ProductWithExpiryDate(Product):

    def __init__(self, name, category_name, unite_price, year_of_production, years_of_validity):
        super().__init__(name=name, category_name=category_name, unite_price=unite_price)
        self._year_of_production = year_of_production
        self._years_of_validity = years_of_validity

    @property
    def year_of_production(self):
        return self._year_of_production

    @property
    def years_of_validity(self):
        return self._years_of_validity

    def does_expire(self, current_year):
        return self._year_of_production + self._years_of_validity < current_year
