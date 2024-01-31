from Shop.Product import Product
from dataclasses import dataclass


@dataclass
class ProductWithExpiryDate(Product):
    years_of_validity: int

    @property
    def year_of_production(self):
        return self.year_of_production

    @property
    def years_of_validity(self):
        return self.years_of_validity

    def does_expire(self, current_year):
        return self.year_of_production + self.years_of_validity < current_year
