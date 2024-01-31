from dataclasses import dataclass


@dataclass
class Apple:
    species_name: str
    size: float
    price_per_kg: float

    def calculate_price(self):
        return self.size * self.price_per_kg

    def __repr__(self):
        return f"<class: Apple, species_name: {self.species_name}, size: {self.size}, price_per_kg: {self.price_per_kg}"
